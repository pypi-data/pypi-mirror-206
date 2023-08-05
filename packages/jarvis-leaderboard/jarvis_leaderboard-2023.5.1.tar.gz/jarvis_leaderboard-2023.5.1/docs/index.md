[LICENSE]: https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst
<!--
<div class="menu-logo">
    <img src="https://www.ctcms.nist.gov/~knc6/static/JARVIS-DFT/images/nist-logo.jpg" alt="" width="100" height="auto"/>
</div>
-->
# JARVIS Leaderboard

This project provides benchmark-performances of various methods for materials science applications using the datasets available in [JARVIS-Tools databases](https://jarvis-tools.readthedocs.io/en/master/databases.html). Some of the methods are: [Artificial Intelligence (AI)](./AI), [Electronic Structure (ES)](./ES), [Force-field (FF)](./FF), [Quantum Computation (QC)](./QC) and [Experiments (EXP)](./EXP). There are a variety of properties included in the benchmark.
In addition to prediction results, we attempt to capture the underlyig software, hardware and instrumental frameworks to enhance reproducibility. This project is a part of the [NIST-JARVIS](https://jarvis.nist.gov) infrastructure.

<!--number_of_methods--> - Number of methods: [98](https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks)

<!--number_of_tasks--> - Number of tasks: 223

<!--number_of_benchmarks--> - Number of benchmarks: 777

<!--number_of_datapoints--> - Number of datapoints: 6934532

<!-- [Learn how to add benchmarks below](#add) -->
<!-- <p style="text-align:center;"><img align="middle" src="https://www.ctcms.nist.gov/~knc6/images/logo/jarvis-mission.png"  width="40%" height="20%"></p>-->




??? question "How to use this website?"

    Check the tabs below:

    === "Learn about the state-of-the-art (SOTA) methods"

        This project provides SOTA methods in 

        + [Artificial Intelligence (AI)](./AI)
             + [SinglePropertyPrediction](./AI/SinglePropertyPrediction)
             + [SinglePropertyClass](./AI/SinglePropertyClass)
             + [ImageClass](./AI/ImageClass)
             + [TextClass](./AI/TextClass)
        + [Electronic Structure (ES)](./ES)
             + [SinglePropertyPrediction](./ES/SinglePropertyPrediction)
             + [Spectra](./ES/Spectra) 
        + [Force-field (FF)](./FF)
             + [SinglePropertyPrediction](./FF/SinglePropertyPrediction)
        + [Qunatum Computation (QC)](./QC)
             + [EigenSolver](./QC/EigenSolver)
        + [Experiments (EXP)](./EXP)
             + [Spectra](./EXP/Spectra)

    === "Adding model benchmarks to existing dataset"
        For a short version, checkout this [google colab-notebook](https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb)

        For a long version, see below:

        1.  [`Fork`](https://github.com/usnistgov/jarvis_leaderboard/fork) the [jarvis_leaderboard](https://github.com/usnistgov/jarvis_leaderboard) repository
        2.  `git clone https://github.com/USERNAME/jarvis_leaderboard`, use your own GitHub USERNAME, e.g. knc6, instead of `usnistgov`

             Note if you do not use forked version, you won't be able to make a pull request
        3.  `cd jarvis_leaderboard`
        4.  `conda create --name leaderboard python=3.8`
        5.  `source activate leaderboard`
        6.  Install the package: `python setup.py develop`
        7.  Let's add abenchmark for Silicon bandgap using DFT PBE (an Electronic structure method) 

          `cd jarvis_leaderboard/benchmarks/`

          `mkdir vasp_pbe_teamX` , you can give any reaosnable name to the benchmark folder in place of `vasp_pbe_teamX`

          `cd  vasp_pbe_teamX`

          `cp ../vasp_optb88vdw/ES-SinglePropertyPrediction-bandgap_JVASP_1002_Si-dft_3d-test-mae.csv.zip .`

          `vi ES-SinglePropertyPrediction-bandgap_JVASP_1002_Si-dft_3d-test-mae.csv.zip`
          
          Note: do not change filenames, e.g., replace dft with qmc etc., which will cause errors

          After pressing eneter twice, you'll see the file content as `id,predictions`

          Just modify the predicting value to your model/measurement value

          Save the file (":wq!" and ":q!")

          Add `metadata.json` and `run.sh` files to capture metadata and enhance reproducibility
       
          Note: An admin will run your `run.sh` to check if he/she can reproduce your benchmark

          Now, `cd ../../../`

          `python jarvis_leaderboard/rebuild.py`

          which will compile all data, compare with reference dataset and calculate metrices

          Hoping there's no error, try: `mkdocs serve`

          Ensure `vasp_pbe_teamX` row exists at:

          `http://127.0.0.1:8000/usnistgov/jarvis_leaderboard/ES/SinglePropertyPrediction/bandgap_JVASP_1002_Si/`

          Now add changes, `git add jarvis_leaderboard/benchmarks/vasp_pbe_teamX`

          Commit your changes, `git commmit -m 'Adding my PBE Si result.'`

          `git push`

          Now go to your forked github repo and make a pull reuqest (PR) to `usnistgov/jarvis_leaderboard` in `develop` branch

          If you are not familiar with pull requests checkout this [link](https://makeapullrequest.com/)
 
          Note: only admins are allowed to make pull requests to `main` branch

          Once the admin approve the PR, you'll see your results on the official leaderboard

        8. Another example for AI mode as follows:

          Populate the dataset for a benchmark, e.g.:

          `python jarvis_leaderboard/populate_data.py --benchmark_file AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test-mae --output_path=Out`

          Train you model(s), e.g.:

          `pip install alignn`

          `wget https://raw.githubusercontent.com/usnistgov/alignn/main/alignn/examples/sample_data/config_example.json`

          `train_folder.py --root_dir "Out" --config "config_example.json" --output_dir="temp"`

          Create a folder in the `jarvis_leaderboard/benchmarks` folder under respective submodule, e.g.:

          `mkdir benchmarks/my_awesome_model`

          Add comma-separated zip file (`.csv.zip`) file(s) corresponding to benchmark(s), e.g.:

          `cp temp/prediction_results_test_set.csv .`

          `mv prediction_results_test_set.csv AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test-mae.csv`

          `zip AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test-mae.csv AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test-mae.csv.zip`

          `mv AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test-mae.csv.zip jarvis_leaderboard/benchmarks/my_awesome_model`
           
          Add metadata info in the `metadata.json` file, e.g.:

          `cp jarvis_leaderboard/benchmarks/alignn_models/metadata.json jarvis_leaderboard/benchmarks/my_awesome_model` 

          Also, add a `run.py`, `run.sh` and `Dockerfile` scripts to reproduce the model predictions.

          Run `python jarvis_leaderboard/rebuild.py` to check there are no errors

          Run `mkdocs serve` to check if the new benchmark exists, e.g. at page
          `http://127.0.0.1:8000/usnistgov/jarvis_leaderboard/AI/SinglePropertyPrediction/exfoliation_energy/`

           Add. commit and push your changes, e.g.:

           `git add jarvis_leaderboard/benchmarks/my_awesome_model`

           `git commit -m 'Adding my awesome_model to jarvis_leaderboard`

           `git push origin main` 
    
          Make a pull request from your fork to the source repo at usnistgov/jarvis_leaderboard `develop` branch

        Notes:

           1. The word: `SinglePropertyPrediction`: task type, `test`, property: `exfoliation_energy`, dataset: `dft_3d`, 
           method: `AI`, metric: `mae` have been joined with '-' sign. This format should be used for consistency in webpage generation.
           
           2. The test data splits are pre-determined, if the exact test IDs are not used, then the code might result in errors.
 

    === "Adding a new dataset and benchmarks"

        1.  Create a `json.zip` file in the `jarvis_leaderboard/dataset` folder under respective submodule, e.g.:

            e.g. `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/dft_3d_exfoliation_energy.json.zip`.      
         
        2.  In the `.json` file should have `train`, `val`, `test` keys with array of ids and their values.
   
            Note `train` and 'val` can be empty dictionaries if the benchmarks are other than AI method

        3.  Add a .md file, e.g.: `jarvis_leaderboard/docs/AI/SinglePropertyPrediction/exfoliation_energy.md`.
   
        4. An example for creating such a file is provided in:
           `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/transform_from_figshare.py`

        5. Then follow the instructions for "Adding model benchmarks to existing dataset"

        Notes:
            We recommend adding your large dataset in Figshare or similar repository and then integrate it in [JARVIS-Tools](https://jarvis-tools.readthedocs.io/en/master/databases.html)
            We also recommend to use JARVIS-Tools for generating dataset/models/benchmarks which can help us maintain the benchmark for long term.       
            Methods used for generating the data and referece are given below:
                <table>
		    <tr>
			<td>Method used for results</td>
			<td>Methods for comparison</td>
		    </tr>
		    <tr>
			<td>EXP</td>
			<td>EXP/ES/analytical results</td>
		    </tr>
		    <tr>
			<td>ES</td>
			<td>ES/EXP</td>
		    </tr>
		    <tr>
			<td>QC</td>
			<td>Classical/analytical results</td>
		    </tr>
		    <tr>
			<td>AI</td>
			<td>Test set data</td>
		    </tr>
                </table>


    === "Acronyms"

        1. [MAE: Mean Absolute Error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)
        2. [ACC: Classification accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
        3. MULTIMAE: MAE sum of multple entries, Euclidean distance
        4. For names of datasets and associated propertiesm refer to datasets in [JARVIS-Tools](https://jarvis-tools.readthedocs.io/en/master/databases.html)

    === "Help"
        Ask a question/raise an [issue on GitHub](https://github.com/usnistgov/jarvis_leaderboard/issues).
        You can also email Kamal Choudhary if needed (kamal.choudhary@nist.gov). However, we recommend using the GitHub issues for any questions/concerns.
       
    === "Citation"
                
		```
                @article{choudhary2020joint,
		  title={The joint automated repository for various integrated simulations (JARVIS) for data-driven materials design},
		  author={Choudhary, Kamal and Garrity, Kevin F and Reid, Andrew CE and DeCost, Brian and Biacchi, Adam J and Hight Walker, Angela R and Trautt, Zachary and Hattrick-Simpers, Jason and Kusne, A Gilad and Centrone, Andrea and others},
		  journal={npj computational materials},
		  volume={6},
		  number={1},
		  pages={173},
		  year={2020},
		  publisher={Nature Publishing Group UK London}
		}
                ```
 
# Example benchmarks

<!--table_content--><table style="width:100%" id="j_table"><thead><tr><th>Method</th><th>Task</th><th>Property</th><th>Model name</th><th>Metric</th><th>Score</th><th>Team</th><th>Dataset</th><th>Size</th></tr></thead><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/ssub_formula_energy" target="_blank">ssub_formula_energy</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/matminer_lgbm" target="_blank">matminer_lgbm</a></td><td>MAE</td><td>0.144</td><td>Matminer</td><td>ssub</td><td>1726</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/dft_3d_formation_energy_peratom" target="_blank">dft_3d_formation_energy_peratom</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>MAE</td><td>0.033</td><td>JARVIS</td><td>dft_3d</td><td>55713</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/dft_3d_optb88vdw_bandgap" target="_blank">dft_3d_optb88vdw_bandgap</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>MAE</td><td>0.142</td><td>JARVIS</td><td>dft_3d</td><td>55713</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/dft_3d_optb88vdw_total_energy" target="_blank">dft_3d_optb88vdw_total_energy</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>MAE</td><td>0.037</td><td>JARVIS</td><td>dft_3d</td><td>55713</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/dft_3d_bulk_modulus_kv" target="_blank">dft_3d_bulk_modulus_kv</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>MAE</td><td>10.399</td><td>JARVIS</td><td>dft_3d</td><td>19680</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyClass" target="_blank">SinglePropertyClass</a></td><td><a href="./AI/SinglePropertyClass/dft_3d_optb88vdw_bandgap" target="_blank">dft_3d_optb88vdw_bandgap</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>ACC</td><td>0.933</td><td>JARVIS</td><td>dft_3d</td><td>55713</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/qm9_std_jctc_LUMO" target="_blank">qm9_std_jctc_LUMO</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>MAE</td><td>0.018</td><td>JARVIS</td><td>qm9_std_jctc</td><td>130829</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./AI/SinglePropertyPrediction/hmof_max_co2_adsp" target="_blank">hmof_max_co2_adsp</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignn_model" target="_blank">alignn_model</a></td><td>MAE</td><td>0.477</td><td>JARVIS</td><td>hmof</td><td>137651</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/MLFF" target="_blank">MLFF</a></td><td><a href="./AI/MLFF/alignn_ff_db_energy" target="_blank">alignn_ff_db_energy</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/alignnff_wt0.1" target="_blank">alignnff_wt0.1</a></td><td>MAE</td><td>0.034</td><td>JARVIS</td><td>alignn_ff_db</td><td>307111</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/ImageClass" target="_blank">ImageClass</a></td><td><a href="./AI/ImageClass/stem_2d_image_bravais_class" target="_blank">stem_2d_image_bravais_class</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/densenet_model" target="_blank">densenet_model</a></td><td>ACC</td><td>0.83</td><td>JARVIS</td><td>stem_2d_image</td><td>9150</td></tr><tr><td><a href="./AI" target="_blank">AI</a></td><td><a href="./AI/TextClass" target="_blank">TextClass</a></td><td><a href="./AI/TextClass/arXiv_categories" target="_blank">arXiv_categories</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/svc_model_text_abstract" target="_blank">svc_model_text_abstract</a></td><td>ACC</td><td>0.908</td><td>ChemNLP</td><td>arXiv</td><td>100994</td></tr><tr><td><a href="./FF" target="_blank">FF</a></td><td><a href="./FF/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./FF/SinglePropertyPrediction/dft_3d_bulk_modulus_JVASP_816_Al" target="_blank">dft_3d_bulk_modulus_JVASP_816_Al</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/NiAlH_jea.eam.alloy" target="_blank">NiAlH_jea.eam.alloy</a></td><td>MAE</td><td>0.027</td><td>JARVIS-FF</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_bulk_modulus_JVASP_816_Al" target="_blank">dft_3d_bulk_modulus_JVASP_816_Al</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_optcx13" target="_blank">vasp_optcx13</a></td><td>MAE</td><td>0.2</td><td>JARVIS</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_bulk_modulus" target="_blank">dft_3d_bulk_modulus</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_opt86b" target="_blank">vasp_opt86b</a></td><td>MAE</td><td>4.662</td><td>JARVIS</td><td>dft_3d</td><td>21</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_bulk_modulus_JVASP_1002_Si" target="_blank">dft_3d_bulk_modulus_JVASP_1002_Si</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/qmcpack_dmc_pbe" target="_blank">qmcpack_dmc_pbe</a></td><td>MAE</td><td>1.05</td><td>JARVIS</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_bandgap" target="_blank">dft_3d_bandgap</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_tbmbj" target="_blank">vasp_tbmbj</a></td><td>MAE</td><td>0.498</td><td>JARVIS</td><td>dft_3d</td><td>54</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_bandgap_JVASP_1002_Si" target="_blank">dft_3d_bandgap_JVASP_1002_Si</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_tbmbj" target="_blank">vasp_tbmbj</a></td><td>MAE</td><td>0.107</td><td>JARVIS</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_epsx" target="_blank">dft_3d_epsx</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_optb88vdw_linopt" target="_blank">vasp_optb88vdw_linopt</a></td><td>MAE</td><td>1.464</td><td>JARVIS</td><td>dft_3d</td><td>16</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_Tc_supercon_JVASP_1151_MgB2" target="_blank">dft_3d_Tc_supercon_JVASP_1151_MgB2</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/qe_pbesol_gbrv" target="_blank">qe_pbesol_gbrv</a></td><td>MAE</td><td>6.315</td><td>JARVIS</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_Tc_supercon" target="_blank">dft_3d_Tc_supercon</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/qe_pbesol_gbrv" target="_blank">qe_pbesol_gbrv</a></td><td>MAE</td><td>3.378</td><td>JARVIS</td><td>dft_3d</td><td>14</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/SinglePropertyPrediction" target="_blank">SinglePropertyPrediction</a></td><td><a href="./ES/SinglePropertyPrediction/dft_3d_slme" target="_blank">dft_3d_slme</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_tbmbj" target="_blank">vasp_tbmbj</a></td><td>MAE</td><td>5.093</td><td>JARVIS</td><td>dft_3d</td><td>5</td></tr><tr><td><a href="./ES" target="_blank">ES</a></td><td><a href="./ES/Spectra" target="_blank">Spectra</a></td><td><a href="./ES/Spectra/dft_3d_dielectric_function" target="_blank">dft_3d_dielectric_function</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/vasp_tbmbj" target="_blank">vasp_tbmbj</a></td><td>MULTIMAE</td><td>11.52</td><td>JARVIS</td><td>dft_3d</td><td>4</td></tr><tr><td><a href="./QC" target="_blank">QC</a></td><td><a href="./QC/EigenSolver" target="_blank">EigenSolver</a></td><td><a href="./QC/EigenSolver/dft_3d_electron_bands_JVASP_816_Al_WTBH" target="_blank">dft_3d_electron_bands_JVASP_816_Al_WTBH</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/qiskit_vqd_SU2_c6" target="_blank">qiskit_vqd_SU2_c6</a></td><td>MULTIMAE</td><td>0.003</td><td>JARVIS</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./EXP" target="_blank">EXP</a></td><td><a href="./EXP/Spectra" target="_blank">Spectra</a></td><td><a href="./EXP/Spectra/dft_3d_XRD_JVASP_19821_MgB2" target="_blank">dft_3d_XRD_JVASP_19821_MgB2</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/bruker_d8" target="_blank">bruker_d8</a></td><td>MULTIMAE</td><td>0.02</td><td>JARVIS</td><td>dft_3d</td><td>1</td></tr><tr><td><a href="./EXP" target="_blank">EXP</a></td><td><a href="./EXP/Spectra" target="_blank">Spectra</a></td><td><a href="./EXP/Spectra/nist_isodb_co2_RM_8852" target="_blank">nist_isodb_co2_RM_8852</a></td><td><a href="https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/10.1007s10450-018-9958-x.Lab01" target="_blank">10.1007s10450-018-9958-x.Lab01</a></td><td>MULTIMAE</td><td>0.021</td><td>JARVIS</td><td>nist_isodb</td><td>1</td></tr><!--table_content--></table>

<!--
<a name="add"></a>
# Adding benchmarks and datasets

To get started, first fork this repository by clicking on the [`Fork`](https://github.com/knc6/jarvis_leaderboard/fork) button. 

Then, clone your forked repository and install the project. Note instead of knc6, use your own username,

```
git clone https://github.com/knc6/jarvis_leaderboard
cd jarvis_leaderboard
python setup.py develop
```

## A) Adding model benchmarks to existing dataset

     To add a new benchmark, 

     1) Populate the dataset for a particular exisiting benchmar e.g.:
     `python jarvis_leaderboard/populate_data.py --benchmark_file SinglePropertyPrediction-test-exfoliation_energy-dft_3d-AI-mae --output_path=Out`
      This will generate an `id_prop.csv` file in the `Out` directory and other pertinent files such as POSCAR files for atomistic properties.
      The code will also print number of training, val and test samples.
      For methods other than AI method, only test set is provided.
      The reference data for ES is from experiments only.

     2) Develop your model(s) using this dataset, e.g.:
     `pip install alignn`
     `train_folder.py --root_dir "Out" --config "alignn/examples/sample_data/config_example.json" --output_dir=temp`

     3) Create a folder in the `jarvis_leaderboard/benchmarks` folder under respective submodule e.g. `xyz_model`. 

     4) In the `xyz_model` folder, add comma-separated zip file (`.csv.zip`) file(s) corresponding to benchmark(s), 
     e.g. `SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv.zip` for `exfoliation_energy` in `dft_3d`
     dataset for `test` split using an `AI` (artificial intelligence method) with 
     `mae` (mean absolute error) metric for `SinglePropertyPrediction` (single property prediction) task. 
     Therefore, the filename should have these six components. 

     Note the word: `SinglePropertyPrediction`: task type, `test`, property: `exfoliation_energy`, dataset: `dft_3d`, 
     method: `AI`, metric: `mae` have been joined with '-' sign. 
     This format should be used for consistency in webpage generation.
     The test data splits are pre-determined, if the exact test IDs are not used, then the code might result in errors. 


     5) Add at least two columns: `id` and `prediction` in the csv file using your model. 
     The `jarvis_leaderboard/rebuild.py` script will parse the data in the csv.zip file, and
     will calculate and analyze several metrics. 
     The `id `should be identifier in the test split set and `prediction` is your model prediction.

     e.g.: for the above alignn example:
     `cp temp/prediction_results_test_set.csv SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv`
     Then zip the file:
     `zip SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv.zip SinglePropertyPrediction-test-exfoliation_energy-dft_2d-AI-mae.csv`

     We recommend to name this folder as your model name, e.g. `alignn_models`, `cfid_models`, `cgcnn_models` etc. 

     6) Add metadata info in the `metadata.json` file, an example is given in the 
     `jarvis_leaderboard/benchmarks/alignn_models/metadata.json`. 
     Also, add a `run.py` and `run.sh` scripts to reproduce the model predictions.
   
     The `project_url` in metadata.json should have link to a paper/GitHub URL.

     7) Make a pull-request to the original repo.

## B) Adding model benchmarks and a new dataset

     To add a new dataset

     1) Create a `json.zip` file in the `jarvis_leaderboard/dataset` folder under respective submodule 
     e.g. `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/dft_3d_exfoliation_energy.json.zip`.

     2) In the `.json` file should have `train`, `val`, `test` keys with array of ids and their values. 
     An example for creating such a file is provided in `jarvis_leaderboard/dataset/AI/SinglePropertyPrediction/format_data.py` 

     3) Add a `.md` file in `docs` folder with path to respective submodule e.g., 
     `docs/AI/SinglePropertyPrediction/exfoliation_energy.md` 

-->


# Summary table





<!--summary_table--><table style="width:100%" id="j_table"><thead><td>Methods</td><td>SinglePropertyPrediction</td><td>SinglePropertyClass</td><td>MLFF</td><td>TextClass</td><td>ImageClass</td><td>Spectra</td><td>EigenSolver</td><tr><td>AI</td><td><a href="./AI/SinglePropertyPrediction" target="_blank">137</a></td><td><a href="./AI/SinglePropertyClass" target="_blank">7</a></td><td><a href="./AI/MLFF" target="_blank">42</a></td><td><a href="./AI/TextClass" target="_blank">18</a></td><td><a href="./AI/ImageClass" target="_blank">2</a></td><td><a href="./AI/Spectra" target="_blank">1</a></td><td>-</td><tr><tr><td>ES</td><td><a href="./ES/SinglePropertyPrediction" target="_blank">501</a></td><td>-</td><td>-</td><td>-</td><td>-</td><td><a href="./ES/Spectra" target="_blank">10</a></td><td>-</td><tr><tr><td>FF</td><td><a href="./FF/SinglePropertyPrediction" target="_blank">47</a></td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><tr><tr><td>QC</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td><a href="./QC/EigenSolver" target="_blank">6</a></td><tr><tr><td>EXP</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td><a href="./EXP/Spectra" target="_blank">6</a></td><td>-</td><tr></table>

# License
   This template is served under the NIST license.  
   Read the [LICENSE] file for more info.