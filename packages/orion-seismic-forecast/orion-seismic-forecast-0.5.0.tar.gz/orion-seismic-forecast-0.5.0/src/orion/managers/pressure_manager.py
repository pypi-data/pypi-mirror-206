# ------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2020-, Lawrence Livermore National Security, LLC
# All rights reserved
#
# See top level LICENSE, COPYRIGHT, CONTRIBUTORS, NOTICE, and ACKNOWLEDGEMENTS files for details.
# ------------------------------------------------------------------------------------------------
"""
pressure_manager.py
-----------------------
"""

from orion.managers import manager_base
from orion.pressure_models import pretrained_ml_model, radial_flow, pressure_table
from orion.utilities import plot_tools
from orion.utilities.plot_config import gui_colors
import sys
import numpy as np


class PressureManager(manager_base.ManagerBase):
    """
    A class for managing the various pressure
    estimation methods within ORION

    Attributes:
        available_models (list): A comprehensive list of available forecast models

    """

    def setup_class_options(self, **kwargs):
        """
        Pressure manager initialization

        Setup empty data holders, configuration options,
        data sources, and gui configuration

        """

        # Set the shorthand name
        self.short_name = 'Pressure'

        # List of available models
        self.child_classes.append(pretrained_ml_model.PretrainedMLModel)
        self.child_classes.append(radial_flow.RadialFlowModel)
        self.child_classes.append(pressure_table.PressureTableModel)

        # The name and instance of the active pressure model
        self.active_model_name = 'RadialFlowModel'
        self.pressure_model = None
        self.active_pressure_models = {}

        # Other configuration
        self.fluid_injection_source = ''
        self.old_fluid_injection_source = ''

    def setup_user_options(self, **kwargs):
        self.catch_pressure_errors = 1

    def setup_data(self, **kwargs):
        """
        Setup data holders
        """
        # Injection data
        self.N = 0
        self.flow_rate = []
        self.pressure = []
        self.epoch = []

    def setup_interface_options(self, **kwargs):
        """
        Setup interface options
        """
        self.set_visibility_operator()

        # Gui elements
        self.gui_elements = {}

        self.gui_elements['active_model_name'] = {
            'element_type': 'dropdown',
            'label': 'Pressure model',
            'position': [1, 0],
            'values': list(self.children.keys())
        }

        self.gui_elements['catch_pressure_errors'] = {
            'element_type': 'check',
            'label': 'Permissive',
            'position': [3, 0],
            'user': True
        }

        self.figures['map_view'] = {
            'position': [0, 0],
            'layer_config': True,
            'size': (7, 6),
            'extra_axis_size': (1.2, 3.2),
            'extra_axis_N': (2, 1)
        }

    def run(self, grid, well_manager, geologic_model):
        self.logger.debug(f'Running pressure model: {self.active_model_name}')
        if self.active_model_name:
            if self.catch_pressure_errors:
                try:
                    self.pressure_model = self.children[self.active_model_name]
                    self.pressure_model.run(grid, well_manager, geologic_model)

                except AttributeError as error:
                    self.logger.error('    model failed to run')
                    self.logger.error('    message: ', error)
                    self.logger.error(f'    {self.active_model_name}: {sys.exc_info()[-1].tb_lineno}')

                except Exception as exception:
                    self.logger.error('    model failed to run')
                    self.logger.error('    message: ', exception)
                    self.logger.error(f'    {self.active_model_name}: {sys.exc_info()[-1].tb_lineno}')
            else:
                self.pressure_model = self.children[self.active_model_name]
                self.pressure_model.run(grid, well_manager, geologic_model)
        else:
            self.logger.error('Requested model does not exist!')

        # TODO: Iterate over multiple pressure models
        self.active_pressure_models[self.active_model_name] = self.pressure_model

    def generate_plots(self, **kwargs):
        # Collect data
        grid = kwargs.get('grid')
        seismic_catalog = kwargs.get('seismic_catalog')
        pressure = kwargs.get('pressure')
        wells = kwargs.get('wells')
        appearance = kwargs.get('appearance')

        # Estimate pressure at the end of the time range
        ts = (grid.snapshot_time * 60 * 60 * 24.0)
        x_range, y_range = grid.get_plot_range()

        # Find the well locations
        well_x, well_y, well_z = wells.get_plot_location(grid)

        # Find current seismic locations
        ms_x = np.zeros(0)
        ms_y = np.zeros(0)
        ms_z = np.zeros(0)
        if seismic_catalog:
            seismic_catalog.set_slice(time_range=[-1e99, ts])
            ms_x, ms_y, ms_z = seismic_catalog.get_plot_location(grid)

        # Estimate pressure at the top of the spatial grid
        self.logger.debug('Generating current spatial pressure estimate')
        Nx = len(grid.x)
        Ny = len(grid.y)
        zm = grid.z[0]

        # Evaluate pressure model
        p = np.zeros((Nx, Ny))
        dpdt = np.zeros((Nx, Ny))
        p_range = np.array([0.0, 1.0])
        dpdt_range = np.array([0.0, 1.0])
        if pressure:
            G = np.meshgrid(grid.x, grid.y, [zm], [ts], indexing='ij')
            p = np.reshape(pressure.p(*G), (len(grid.x), len(grid.y)))
            p = np.swapaxes(p, 0, 1)
            dpdt = np.reshape(pressure.dpdt(*G), (len(grid.x), len(grid.y))) * (60 * 60 * 24 * 365.25)
            dpdt = np.swapaxes(dpdt, 0, 1)
            if (appearance.plot_cmap_range == 'global'):
                if (np.size(pressure.p_grid)):
                    p_range[:] = [np.amin(pressure.p_grid[:, :, 0, :]), np.amax(pressure.p_grid[:, :, 0, :])]
                    dpdt_range[:] = [np.amin(pressure.dpdt_grid[:, :, 0, :]), np.amax(pressure.dpdt_grid[:, :, 0, :])]
                    dpdt_range *= (60 * 60 * 24 * 365.25)
            else:
                p_range[:] = [np.amin(p), np.amax(p)]
                dpdt_range[:] = [np.amin(dpdt), np.amax(dpdt)]

        # Choose the scaling, range, labels
        base_units = {-1: 'm', 0: '', 1: 'k', 2: 'M', 3: 'G'}
        p_range = np.array([np.amin(p), np.amax(p)])
        # self.logger.debug(f'p_range = [{p_range[0]:1.1e}, {p_range[1]:1.1e}] Pa')
        p_order = min(int(np.floor(np.log10(max(0.001, np.amax(abs(p_range)))) / 3)), 3)
        p_scale = 10**(3 * p_order)
        p /= p_scale
        p_range /= p_scale
        p_units = f'{base_units[p_order]}Pa'
        # self.logger.debug(f'p_range = [{p_range[0]:1.1e}, {p_range[1]:1.1e}] {p_units}')

        # self.logger.debug(f'dpdt_range = [{dpdt_range[0]:1.1e}, {dpdt_range[1]:1.1e}] Pa/year')
        dpdt_order = min(int(np.floor(np.log10(max(0.001, np.amax(abs(dpdt_range)))) / 3)), 3)
        dpdt_scale = 10**(3 * dpdt_order)
        dpdt /= dpdt_scale
        dpdt_range /= dpdt_scale
        dpdt_units = f'{base_units[dpdt_order]}Pa/year'
        # self.logger.debug(f'dpdt_range = [{dpdt_range[0]:1.1e}, {dpdt_range[1]:1.1e}] {dpdt_units}')

        # Choose a minimum scale size
        if (p_range[1] - p_range[0] < 1e-6):
            p_range[1] += 1.0
        if (dpdt_range[1] - dpdt_range[0] < 1e-6):
            dpdt_range[1] += 1.0

        # Spatial plot
        # Setup axes
        self.logger.debug('Rendering pressure manager spatial plot')
        ax = self.figures['map_view']['handle'].axes[0]
        old_visibility = plot_tools.getPlotVisibility(ax)
        ax.cla()

        cfig = self.figures['map_view']['extra_axis']
        cax = cfig.axes[0]
        cax.cla()
        ca = ax.imshow(dpdt,
                       extent=[x_range[0], x_range[1], y_range[0], y_range[1]],
                       aspect='auto',
                       interpolation='bilinear',
                       label='dpdt',
                       vmin=dpdt_range[0],
                       vmax=dpdt_range[1],
                       cmap=gui_colors.dpdt_colormap,
                       origin='lower',
                       visible=old_visibility['dpdt'])
        plot_tools.setupColorbar(cfig, ca, cax, dpdt_range, f'dpdt ({dpdt_units})')

        cax = self.figures['map_view']['extra_axis'].axes[1]
        cax.cla()
        ca = ax.imshow(p,
                       extent=[x_range[0], x_range[1], y_range[0], y_range[1]],
                       aspect='auto',
                       interpolation='bilinear',
                       label='Pressure',
                       vmin=p_range[0],
                       vmax=p_range[1],
                       cmap=gui_colors.pressure_colormap,
                       origin='lower',
                       visible=old_visibility['Pressure'])
        plot_tools.setupColorbar(cfig, ca, cax, p_range, f'Pressure ({p_units})')

        # Add microseismic locations
        ax.plot(ms_x,
                ms_y,
                label='Microseismic Events',
                visible=old_visibility['Microseismic Events'],
                **gui_colors.microseismic_style)

        # Add well locations
        is_injector = wells.get_injector_flag()
        is_monitor = wells.get_monitor_flag()
        ax.plot(well_x[is_injector],
                well_y[is_injector],
                label='Injector Wells',
                visible=old_visibility['Injector Wells'],
                **gui_colors.well_style)
        # ax.plot(well_x[~is_injector],
        #         well_y[~is_injector],
        #         label='Extraction Wells',
        #         visible=old_visibility['Extraction Wells'],
        #         **gui_colors.extraction_well_style)
        ax.plot(well_x[is_monitor],
                well_y[is_monitor],
                label='Monitor Wells',
                visible=old_visibility['Monitor Wells'],
                **gui_colors.monitor_well_style)

        # Finalize figure
        ax_labels = grid.get_axes_labels()
        ax.set_xlabel(ax_labels[0])
        ax.set_ylabel(ax_labels[1])
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        ax.legend(loc=1)
        ax.set_title(f'Snapshot at t = {grid.snapshot_time:1.1f} days')
