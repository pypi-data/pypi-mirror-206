# Welcome to the ORION Toolkit!

The Operational Forecasting of Induced Seismicity toolkit “ORION”, has been developed to understand and mitigate this risk of inducing earthquakes. Induced seismicity has been recognized as a significant risk faced by carbon storage operations which, in extreme cases, may lead to property damage and complete cessation of storage at a site. Mitigation of this risk first requires an understanding of the current and short-term future seismic hazard.

ORION is an open-source, observation-based ensemble forecasting toolkit which is geared towards helping operators understand the seismic hazard at a site. ORION analyzes how the seismic hazard evolves during injection and suggests possible mitigation strategies to employ if an earthquake that exceeds certain threshold is observed. Through its ensemble modeling approach, ORION leverages the benefits of statistical-, physics-, and machine learning-based forecasting methodologies, while reducing the impact of each model’s respective limitations.

The ORION toolkit consists of an easy-to-use GUI interface that affords a user as much or as little interaction as desired. Advanced capabilities allow the user to upload local, high-precision earthquake catalogs, projected injection profiles and/or spatiotemporal estimates of pressure/stress, and to tune various model parameters. ORION will then provide a spatial and temporal ensemble forecast of seismicity defined as the probability of exceedance of a given earthquake magnitude over a forecast period. Additionally, ORION will provide probability distribution of the statistically derived maximum possible earthquake magnitude that may be expected. Finally, ORION will provide suggested operational management strategies (e.g. reduce injection volumes at specific wells) based on the level of hazard).


## Documentation

Our documentation is hosted [here](https://nrap.gitlab.io/orion/index.html).


## Who develops Orion?

- Lawrence Livermore National Laboratory
- Lawrence Berkeley National Laboratory


## License

Orion is distributed under the terms of the MIT license.
See [LICENSE](https://gitlab.com/NRAP/orion/-/blob/develop/LICENSE),
[COPYRIGHT](https://gitlab.com/NRAP/orion/-/blob/develop/COPYRIGHT),
[NOTICE](https://gitlab.com/NRAP/orion/-/blob/develop/NOTICE), and 
[ACKNOWLEDGEMENTS](https://gitlab.com/NRAP/orion/-/blob/develop/ACKNOWLEDGEMENTS), for details.

LLNL-CODE-842148
