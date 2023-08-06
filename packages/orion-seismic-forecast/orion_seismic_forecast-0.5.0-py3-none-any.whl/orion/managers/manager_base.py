# ------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2020-, Lawrence Livermore National Security, LLC
# All rights reserved
#
# See top level LICENSE, COPYRIGHT, CONTRIBUTORS, NOTICE, and ACKNOWLEDGEMENTS files for details.
# ------------------------------------------------------------------------------------------------
"""
manager_base.py
-----------------------
"""

import json
import logging
import os
from orion.utilities.plot_config import gui_colors
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PIL import ImageColor
try:
    from mpl_toolkits.mplot3d import Axes3D
except:
    pass


class ManagerBase():
    """
    Base manager class for ORION

    Attributes:
        short_name (str): A short name used to be used in the Orion Gui
        child_classes (list): A list of potential children
        children (dict): Dictionary of initialized children
        figures (dict): Dictonary to hold object plot instructions, handles
        N (int): Length of data loaded into manager
        gui_elements (dict): Dictionary of elements to be added to the gui
        cache_root (str): Location of the cache directory
        config_type (str): The style to be applied to the gui configuration (split/unified, default=split)
        plot_cmap_range_options (list): List of potential color map options
        plot_cmap_range (str): Active plot color map option
        logger (self.logging.Logger): The orion logger instance
    """

    def __init__(self, **kwargs):
        """
        Generic manager initialization

        Setup empty data holders, configuration options,
        data sources, and gui configuration

        """
        self.short_name = 'undefined'
        self.child_classes = []
        self.children = {}
        self.figures = {}
        # self.N = 0

        self.cache_root = os.path.expanduser('~/.cache/orion')

        # Gui config
        self.gui_elements = {}
        self.config_type = 'split'
        self.show_plots = True
        self.visible_to_users = ['Super User']

        # Plot config
        self.plot_cmap_range_options = ['current', 'global']
        self.plot_cmap_range = 'current'
        self.figures_require_adjustment = True

        # Logger
        self.logger = logging.getLogger('orion_logger')
        logging.basicConfig(level=logging.WARNING, format='(%(asctime)s %(module)s:%(lineno)d) %(message)s')
        logging.captureWarnings(True)

        # Call user-defined setup steps
        self.setup_class_options(**kwargs)
        self.setup_user_options(**kwargs)
        self.initialize_children()
        self.setup_data(**kwargs)
        self.setup_interface_options(**kwargs)

    def setup_class_options(self, **kwargs):
        """
        Setup class options
        """
        pass

    def setup_user_options(self, **kwargs):
        """
        Setup class options
        """
        pass

    def setup_data(self, **kwargs):
        """
        Setup data holders
        """
        pass

    def setup_interface_options(self, **kwargs):
        """
        Setup interface options
        """
        pass

    def __getstate__(self):
        """
        Ignore pickling certain elements
        """
        state = self.__dict__.copy()
        del state["gui_elements"]
        return state

    def __setstate__(self, state):
        """
        Restore unpickled elements
        """
        self.__dict__.update(state)
        self.gui_elements = {}

    def process_inputs(self):
        """
        Process any required gui inputs
        """
        pass

    def process_inputs_recursive(self):
        """
        Process this object and its children
        """
        self.process_inputs()
        for k in self.children.keys():
            self.children[k].process_inputs_recursive()

    def restore_defaults(self):
        """
        Process this object and its children
        """
        self.__init__()
        for k in self.children.keys():
            self.children[k].restore_defaults()

    def initialize_children(self):
        """
        Create an instance of each object listed in child_classes
        """
        for tmp in self.child_classes:
            child = tmp()
            self.children[type(child).__name__] = child

    def add_child(self, child_name):
        """
        Method to add a new child to the current object by name

        Args:
            child_name (str): The name of the new child
        """
        self.logger.warning(f'Unrecognized child in config: {child_name}')

    def get_config_recursive(self, user=False):
        """
        Convert the model configuration to a dict

        Args:
            user (bool): Flag to indicate whether to save user or general data

        """
        # Get the current level gui configs
        config = {}
        for k in self.gui_elements:
            if self.gui_elements[k].get('user', False) == user:
                config[k] = getattr(self, k)

        # Get the children's configs
        for k in self.children:
            tmp = self.children[k].get_config_recursive(user=user)
            if tmp:
                config[k] = tmp

        return config

    def save_config(self, fname='', user=False):
        """
        Saves the manager config as a json file

        Args:
            fname (str): Name of the target json configuration file
            user (bool): Flag to indicate whether to save user or general data

        """
        config = self.get_config_recursive(user=user)
        with open(fname, 'w') as f:
            json.dump(config, f, indent=4)

    def set_config_recursive(self, config, ignore_attributes=['log_file']):
        """
        Sets the current object's configuration from a
        dictionary or json file

        Args:
            config (dict): The configuration dictionary

        """
        for k in config:
            if k in self.gui_elements:
                # Set gui element values
                try:
                    if k not in ignore_attributes:
                        if config[k] is None:
                            continue

                        # Update dict types in case of changes
                        if isinstance(config[k], dict):
                            tmp = getattr(self, k)
                            tmp.update(config[k])
                            config[k] = tmp

                        setattr(self, k, config[k])
                except KeyError:
                    self.logger.warning(f'Unrecognized parameter in configuration: {k}')

            else:
                # Set child values
                if k not in self.children:
                    self.add_child(k)
                if k in self.children:
                    self.children[k].set_config_recursive(config[k])

    def load_config(self, fname):
        """
        Loads the forecast manager config from a json file

        Args:
            fname (str): Name of the target json configuration file

        """
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                config = json.load(f)
                self.set_config_recursive(config)

    def set_visibility_all(self):
        self.visible_to_users = ['General', 'Specific Earthquake', 'Operator', 'Super User']

    def set_visibility_operator(self):
        self.visible_to_users = ['Operator', 'Super User']

    def load_data(self, grid):
        """
        Load data into the manager

        Args:
            grid (orion.managers.grid_manager.GridManager): The Orion grid manager
        """
        pass

    def setup_figures(self, gui_backend=False):
        """
        Open up figure handles
        """
        for k in self.figures:
            if ('handle' not in self.figures[k]):
                if gui_backend:
                    self.figures[k]['handle'] = Figure(figsize=self.figures[k]['size'], dpi=100)
                else:
                    self.figures[k]['handle'] = plt.figure(figsize=self.figures[k]['size'], dpi=100)
                self.figures[k]['create_axes'] = True

            if ('extra_axis_size' in self.figures[k]):
                if ('extra_axis' not in self.figures[k]):
                    if gui_backend:
                        self.figures[k]['extra_axis'] = Figure(figsize=self.figures[k]['extra_axis_size'], dpi=100)
                    else:
                        self.figures[k]['extra_axis'] = plt.figure(figsize=self.figures[k]['extra_axis_size'], dpi=100)

    def setup_figures_recursive(self, gui_backend=False):
        """
        Recursively open figure handles for orion plots
        This is completed as a separate step from axes and content
        due to an initialization order requirement in the gui

        """
        self.setup_figures(gui_backend=gui_backend)
        for k in self.children:
            self.children[k].setup_figures(gui_backend=gui_backend)

    def setup_figure_axes(self, plot_type):
        """
        Setup any requested figure axes for the current object

        Args:
            plot_type (str): The target dimension for supported plots (2D or 3D)
        """
        for k in self.figures:
            if self.figures[k]['create_axes']:
                self.figures[k]['max_dimension'] = plot_type
                self.figures[k]['create_axes'] = False
                if ('N' in self.figures[k]):
                    N = self.figures[k]['N']
                    for ii in range(N[0] * N[1]):
                        self.figures[k]['handle'].add_subplot(N[0], N[1], ii + 1)
                else:
                    if (('3D_option' in self.figures[k]) and (plot_type == '3D')):
                        self.figures[k]['handle'].add_subplot(1, 1, 1, projection='3d')
                        self.figures[k]['current_dimension'] = '3D'
                    else:
                        self.figures[k]['handle'].add_subplot(1, 1, 1)
                        self.figures[k]['current_dimension'] = '2D'

                if ('extra_axis_size' in self.figures[k]):
                    if ('extra_axis_N' in self.figures[k]):
                        N = self.figures[k]['extra_axis_N']
                        for ii in range(N[0] * N[1]):
                            self.figures[k]['extra_axis'].add_subplot(N[0], N[1], ii + 1)
                    else:
                        self.figures[k]['extra_axis'].add_subplot(1, 1, 1)

        # Check to see if the figure axes match the expected dimensions
        regenerate_axes = False
        for k in self.figures:
            if (plot_type != self.figures[k]['max_dimension']):
                if ('3D_option' in self.figures[k]):
                    regenerate_axes = True

        if regenerate_axes:
            self.reset_figures()
            self.setup_figure_axes(plot_type)
            self.update_figure_colors()

    def update_figure_colors(self):
        """
        Update figure colors that are not set by rcParams.update()
        """
        for kb in self.figures:
            # Main figure
            self.figures[kb]['handle'].patch.set_facecolor(gui_colors.theme['background_1'])

            if self.figures[kb].get('current_dimension', '2D') == '3D':
                ax = self.figures[kb]['handle'].axes[0]
                ax.set_facecolor(gui_colors.theme['background_1'])
                rgb = ImageColor.getcolor(gui_colors.theme['foreground_0'], "RGB")
                axis_color = (rgb[0] / 256.0, rgb[1] / 256.0, rgb[2] / 256.0, 0.0)
                ax.w_xaxis.set_pane_color(axis_color)
                ax.w_yaxis.set_pane_color(axis_color)
                ax.w_zaxis.set_pane_color(axis_color)

            # Extra_axis
            if ('extra_axis' in self.figures[kb]):
                self.figures[kb]['extra_axis'].patch.set_facecolor(gui_colors.theme['background_1'])

    def close_figures(self):
        """
        Close the open figures associated with the current manager
        """
        for ka in self.figures:
            for kb in ['handle', 'extra_axis']:
                if (kb in self.figures[ka]):
                    # self.figures[ka][kb].close()
                    del self.figures[ka][kb]

    def close_figures_recursive(self):
        """
        Recursively close the figures associated with the current manager and its children
        """
        self.close_figures()
        for k in self.children.keys():
            self.children[k].close_figures_recursive()

    def clear_data(self):
        """
        Clear any collected data
        """
        self.setup_class_options()
        self.setup_data()

    def clear_data_recursive(self):
        """
        Recursively clear data associated with the current manager and its children
        """
        self.clear_data()
        for k in self.children.keys():
            self.children[k].clear_data_recursive()

    def reset_figures(self):
        """
        Reset the open figures associated with the current manager
        """
        for f in self.figures.values():
            f['create_axes'] = True
            f['handle'].clf()
            if ('extra_axis_size' in f):
                f['extra_axis'].clf()

            if ('colorbar' in f):
                del f['colorbar']

    def reset_figures_recursive(self):
        """
        Recursively reset the figures associated with the current manager and its children
        """
        self.reset_figures()
        for k in self.children.keys():
            self.children[k].reset_figures_recursive()

    def adjust_figure_axes(self):
        """
        Apply formatting to the figures on the current object
        """
        if self.figures_require_adjustment:
            self.figures_require_adjustment = False
        else:
            return

        for k in self.figures:
            try:
                self.figures[k]['handle'].tight_layout()
            except:
                pass

            if ('extra_axis' in self.figures[k]):
                try:
                    self.figures[k]['extra_axis'].tight_layout()
                except:
                    pass

    def generate_plots(self, **kwargs):
        """
        Generate any plots for the current object

        Keyword Args:
            grid (orion.managers.grid_manager.GridManager): The Orion grid manager
            seismic_catalog (orion.managers.seismic_catalog.SeismicCatalog): The current seismic catalog
            pressure (orion.pressure_models.pressure_model_base.PressureModelBase): The current pressure model
            wells (orion.managers.well_manager.WellManager): The well data
            forecasts (orion.managers.forecast_manager.ForecastManager): Forecast data
            appearance (orion.managers.apperance_manager.AppearanceManager): Appearance options
        """
        pass

    def update_plot_data(self, grid, seismic_catalog, pressure, wells):
        """
        Update plot data for current object

        Args:
            grid (orion.managers.grid_manager.GridManager): The Orion grid manager
            seismic_catalog (orion.managers.seismic_catalog.SeismicCatalog): The current seismic catalog
            pressure (orion.pressure_models.pressure_model_base.PressureModelBase): The current pressure model
            wells (orion.managers.well_manager.WellManager): The well data
        """
        pass

    def generate_plots_recursive(self, **kwargs):
        """
        Recursively generate any plots for the current object

        Keyword Args:
            grid (orion.managers.grid_manager.GridManager): The Orion grid manager
            seismic_catalog (orion.managers.seismic_catalog.SeismicCatalog): The current seismic catalog
            pressure (orion.pressure_models.pressure_model_base.PressureModelBase): The current pressure model
            wells (orion.managers.well_manager.WellManager): The well data
            forecasts (orion.managers.forecast_manager.ForecastManager): Forecast data
            appearance (orion.managers.apperance_manager.AppearanceManager): Appearance options
        """
        self.setup_figure_axes(kwargs['appearance'].active_plot_types)
        if self.show_plots:
            self.generate_plots(**kwargs)
            self.adjust_figure_axes()
        for k in self.children:
            self.children[k].generate_plots_recursive(**kwargs)

    def update_plot_data_recursive(self, grid, seismic_catalog, pressure, wells):
        """
        Recursively update plot data for the current object

        Args:
            grid (orion.managers.grid_manager.GridManager): The Orion grid manager
            grid (orion.managers.seismic_catalog.SeismicCatalog): The current seismic catalog
            seismic_catalog (orion.pressure_models.pressure_model_base.PressureModelBase): The current pressure model
            wells (orion.managers.well_manager.WellManager): The well data
        """
        self.update_plot_data(grid, seismic_catalog, pressure, wells)
        for k in self.children:
            self.children[k].update_plot_data_recursive(grid, seismic_catalog, pressure, wells)

    def save_figures(self, output_path, dpi=400, plot_list=[], suffix='', save_legends=True, status=None):
        """
        Save figures

        Args:
            output_path (str): Path to place output figures
            dpi (int): Resolution of the output figures
        """
        if status is not None:
            status.set('Rendering figures')

        os.makedirs(output_path, exist_ok=True)
        for k, fig in self.figures.items():
            fig['handle'].savefig(os.path.join(output_path, f'{k}{suffix}.png'), dpi=dpi)
            if (('extra_axis' in fig) and save_legends):
                fig['extra_axis'].savefig(os.path.join(output_path, f'legend_{k}{suffix}.png'), dpi=dpi)

        # Save child object figures
        for k in self.children:
            if (len(plot_list) == 0) or (k in plot_list):
                self.children[k].save_figures(output_path, suffix=suffix, save_legends=save_legends)

        if status is not None:
            status.set('')
