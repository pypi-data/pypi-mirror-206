from .mixcr_nils import process_mixcr
from ast import literal_eval
import os
from .load_data import collectFiles
from .loop_collect_reports import load_mixed_files, load_alignment_reports
import pandas as pd
from glob import glob
from .check_reports import check_completeness
import sys
import pickle
import pkg_resources
from .trimming import trimming
try:
    import tkinter as tk
    from tkinter import filedialog
except:
    pass

def pull_seq_align_repo():
    try:
        print("choose the directory where you store your alignment reports and your sequencing report")
        filenames_dir = filedialog.askdirectory()
        filenames = glob(filenames_dir + "//*")
        for i in filenames:
            if os.path.isdir(i):
                if "alignment_reports" in i:
                    alignment_repos = glob(i)
                    filenames.extend(alignment_repos)
    except:
        filenames_dir = input(
            "Enter the directory where you store the alignment reports and your sequencing report manually.")
        filenames_dir = os.path.abspath(filenames_dir)
        filenames = glob(filenames_dir)
        for i in filenames:
            if os.path.isdir(i):
                if "alignment_reports" in i:
                    alignment_repos = glob(i)
                    filenames.extend(alignment_repos)
    sequencing_report, all_alignment_reports = load_mixed_files(filenames)
    return sequencing_report, all_alignment_reports

def check_experiment(module_dir):
    while True:
        experiment = input("How do you want to call your new experiment?")
        if os.path.isdir(os.path.join(module_dir, "my_experiments", experiment)) == True:
            replace = input("The given directory already exists. Do you want to replace it? (Y/n)")
            if replace in ["Y", "y", "n", "N"]:
                break
            else:
                print("Please enter another name.")
        else:

            os.mkdir(os.path.join(module_dir,
                                       "my_experiments",
                                       experiment))
            break
    return experiment

def method_one(experiment, repo_path, module_dir):
    use_method = input(
        "Per default you will align your data with the following method: milab-human-tcr-dna-multiplex-cdr3 . Press enter if you want to continue. Otherwise type in the method of your choice which. It has to be the exact same string which is given on the Mixcr documentation.")
    if use_method == "":
        method = "milab-human-tcr-dna-multiplex-cdr3"
    else:
        method = use_method
    paired_end = input("Do you want to analyze paired_end_sequencing data? (Y/n)")
    if paired_end.lower() in ["Y", "y"]:
        paired_end = True
    else:
        paired_end = False
    process_mixcr(experiment,
                  method=method,
                  paired_end_sequencing=paired_end)

    with open(repo_path, "rb") as f:
        sequencing_report = pd.read_table(f, sep=",")
    try:
        align_repo_path = os.path.join(module_dir,
                                       "my_experiemnts",
                                       experiment,
                                       "alignment_reports",
                                       "*")
        alignment_reports = glob(align_repo_path)
        all_alignment_reports = load_alignment_reports(alignment_reports)
    except:
        all_alignment_reports = pd.DataFrame([])
        print(
            "No alignment reports could be found in " + experiment + ". You will continue without being able to analyze the Alignment Quality.")
    return sequencing_report, all_alignment_reports
def method_two(module_dir, experiment):

    print("Choose the folder which contains the sequencing_report and the alignment reports.")

    sequencing_report, all_alignment_reports = pull_seq_align_repo()

    while True:
        if sequencing_report.shape[0] == 0:
            print(
                "Something went wrong. Unfortunately you could not collect the data in the sequencing report. Please make sure that you have chosen the right directory and that you have tsv files as output from mixcr in that directory.")
            sequencing_report, all_alignment_reports = pull_seq_align_repo()
        else:
            break
        #  sys.exit()
    while True:
        trim_data = input("Do you need to trim your data? (Y/n)")
        if trim_data in ["Y", "y", "n", "N"]:
            break
        else:
            print("Please enter a correct value.")
    if trim_data.lower() in ["Y", "y"]:
        sequencing_report = trimming(sequencing_report,
                                     divisible_by=3,  # might be possible that columns are different
                                     min_count=1,
                                     new_fraction="cloneFraction")
    else:
        pass
    seq_report_dir = os.path.join(module_dir,
                                  "my_experiments",
                                  experiment,
                                  "sequencing_report.csv")
    sequencing_report.to_csv(seq_report_dir)
    unique_experiments = sequencing_report["Experiment"].unique()
    experiment_dic = {item: item for item in list(unique_experiments)}
    exp_names_dir = os.path.join(module_dir,
                                 "my_experiments",
                                 experiment,
                                 "experiment_names.pickle")
    with open(exp_names_dir, "wb") as f:
        pickle.dump(experiment_dic, f)

    if all_alignment_reports.shape[0] == 0:
        print(
            "No Alignment Reports were uploaded. You will continue the analysis without being able to analyze the Alignment Quality.")
    else:
        try:
            all_alignment_reports = check_completeness(all_alignment_reports, sequencing_report)
        except:
            pass
    exp_name_path = os.path.join(module_dir,
                                 "my_experiments",
                                 experiment,
                                 "experiment_names.pickle")

    unique_experiments = sequencing_report["Experiment"].unique()
    experiment_dic = {item: item for item in list(unique_experiments)}

    with open(exp_name_path, "wb") as f:
        pickle.dump(experiment_dic, f)
    return sequencing_report, all_alignment_reports

def method_three():
    try:
        print("choose the file where you store your sequencing report")
        f = filedialog.askopenfilename()
        sequencing_report = pd.read_table(f, sep=",")
    except:
        while True:
            f = input("give the path to your file which is the sequencing report")
            f = os.path.abspath(f)
            if os.path.isfile(f):
                sequencing_report = pd.read_table(f, sep=",")
                break
            else:
                print("Sorry, but the filepath you entered is invalid.")
    all_alignment_reports = None
    return sequencing_report,all_alignment_reports

def check_last_exp(pkg_path, module_dir):
    glob_vars = os.path.join(pkg_path,
                             "settings",
                             "global_vars.txt")
    with open(glob_vars, "r") as f:
        data = f.read()
    data = literal_eval(data)

    last_experiment = data["last_experiment"]
    repo_path = os.path.join(module_dir,
                             "my_experiments",
                             "last_experiment",
                             "sequencing_report.txt")
    return repo_path, last_experiment
def upload():
    module_dir = os.path.abspath("")
    pkg_path = pkg_resources.resource_filename("ExpoSeq", "")
    repo_path, last_experiment = check_last_exp(pkg_path, module_dir)

    if os.path.isfile(repo_path):
        continue_analysis = input("Do you want to continue to analyze with " + last_experiment + "? Y/n")
        if continue_analysis.lower() in ["n", "N"]:
            next_step = input("If you want to upload a new experiment press 1. If you want to choose another experiment press 2")
            if next_step == "1":
                experiment = check_experiment(module_dir)

                choose_method = input("If you want to process your data with mixcr press 1. If you want to upload already processed txt files with unique clones, press 2")
                if choose_method == "1":
                    sequencing_report, all_alignment_reports = method_one(experiment, repo_path, module_dir)
                if choose_method == "2":
                    sequencing_report, all_alignment_reports = method_two(module_dir, experiment)


                if choose_method == "3":
                    sequencing_report, all_alignment_reports = method_three()

            if next_step == "2":
                while True:
                    user_input = input("Enter the name of the experiment you want to analyze")

                    user_input = user_input  # Try to convert the input to an integer
                    spec_exp_name_path = os.path.join(module_dir,
                                                      "my_experiments",
                                                      user_input)
                    if os.path.isdir(spec_exp_name_path):  # Check if the input is in the correct range
                        break  # If the input is valid, break out of the loop
                    else:
                        print("The experiment name does not exist in my_experiments. Please enter the correct name")
                experiment = user_input
                seq_report_path = os.path.join(module_dir,
                                               "my_experiments",
                                               experiment,
                                               "sequencing_report.txt")
                with open(seq_report_path, "rb") as f:
                    sequencing_report = pd.read_table(f, sep=",")
                try:
                    align_repo_path = os.path.join(module_dir,
                                                   "my_experiments",
                                                   experiment,
                                                   "alignment_reports",
                                                   "*")
                    alignment_reports = glob(align_repo_path)
                    all_alignment_reports = load_alignment_reports(alignment_reports)
                except:
                    all_alignment_reports = pd.DataFrame([])
                    print(
                        "No alignment reports could be found in " + experiment + ". You will continue without being able to analyze the Alignment Quality.")

            else:
                pass
        else:
            experiment = last_experiment
            seq_report_path = os.path.join(module_dir,
                                           "my_experiments",
                                           experiment,
                                           "sequencing_report.txt")
            with open(seq_report_path, "rb") as f:
                sequencing_report = pd.read_table(f, sep=",")
            try:
                align_repo_path = os.path.join(module_dir,
                                               "my_experiments",
                                               experiment,
                                               "alignment_reports",
                                               "*")
                alignment_reports = glob(align_repo_path)
                all_alignment_reports = load_alignment_reports(alignment_reports)
            except:
                all_alignment_reports = pd.DataFrame([])
                print(
                    "No alignment reports could be found in " + experiment + ". You will continue without being able to analyze the Alignment Quality.")

    else:

        choose_method = input("Welcome to ExpoSeq. If you want to start by processing your fastq files with mixcr press 1. If you want to upload already processed files press 2. If you want to upload a sequencing report press 3.")
        experiment = check_experiment(module_dir)
        if choose_method == "1":
            sequencing_report, all_alignment_reports = method_one(experiment, repo_path, module_dir)
        else:
            pass
        if choose_method == "2":
            sequencing_report, all_alignment_reports = method_two(module_dir, experiment)
        if choose_method == "3":
            sequencing_report, all_alignment_reports = method_three()

    return sequencing_report, all_alignment_reports, experiment