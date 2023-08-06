import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.metrics import roc_auc_score


def plot_confusion_matrix(y_true,y_pred,title_prefix="Confusion Matrix",cbar_flag=True,target_names=None,savefig_path=None):
    #plt.figure(facecolor=(1, 1, 1))
    #plt.tight_layout(pad=2)
    acc = accuracy_score(y_true,y_pred)
    confusion_matrix_value = confusion_matrix(y_true, y_pred)
    cm_array_df = pd.DataFrame(confusion_matrix_value)
    
    if target_names != None:        
        if target_names == True:
            unique_labels = y_true.unique()
            unique_labels.sort()
            unique_labels = [str(x) for x in unique_labels]
            target_names = unique_labels
            
        cm_array_df = pd.DataFrame(confusion_matrix_value, index=target_names, columns=target_names) # replacing index and columns name with the labels name we want to display
        # print target labels name like class 0, class 1, class 2
        sn_fig=sns.heatmap(cm_array_df, square=True, annot=True, fmt='d', cbar=cbar_flag,cmap="YlGnBu",vmin=np.min(confusion_matrix_value),vmax=np.max(confusion_matrix_value))
        sn_fig.set_xticklabels(sn_fig.get_xticklabels(), rotation = 30)#, fontsize = 8
        sn_fig.set_yticklabels(sn_fig.get_yticklabels(), rotation = 0)#, fontsize = 8
    else:
        # print target labels like 0, 1, 2
        sn_fig = sns.heatmap(confusion_matrix_value, square=True, annot=True, fmt='d', cbar=cbar_flag,cmap="YlGnBu",vmin=np.min(confusion_matrix_value),vmax=np.max(confusion_matrix_value))
        #sn_fig.set_xticklabels(sn_fig.get_xticklabels(), rotation = 45)#, fontsize = 8
    
    plt.xlabel('Predicted Values')
    plt.ylabel('True Values')
    plt.title(str(title_prefix) + "\nAccuracy = "+str(round(acc,3)))
    plt.tight_layout()
    if savefig_path!=None:
        plt.savefig(savefig_path,bbox_inches='tight',dpi=200)
    # precision and recall
    #https://towardsdatascience.com/confusion-matrix-for-your-multi-class-machine-learning-model-ff9aa3bf7826
    print('\nClassification Report\n')
    print(classification_report(y_true,y_pred, target_names=target_names))
    return savefig_path , acc, cm_array_df
#     return plt
#---------------------------------------------------------------------------------------------------
def binary_classification(data,combine_labels_upto):
    # considering 1,2 to class 0 and other to class 1
    binarized_data = [0 if x<=combine_labels_upto else 1 for x in data]
    return pd.Series(binarized_data)
#---------------------------------------------------------------------------------------------------
def combine_classes_for_classification(data,combine_labels=[2,3,4]):
    # considering 0,1,2 class where 2 is combination of combine_labels=[2,3,4]
    combine_classes = [min(combine_labels) if x in combine_labels else int(x) for x in data]
    return pd.Series(combine_classes)
#---------------------------------------------------------------------------------------------------
def binary_classification_with_coefficient(data,coeff):
    # divide based on coeff value
    binarized_data = [0 if x<=coeff else 1 for x in data]
    return pd.Series(binarized_data)

#---------------------------------------------------------------------------------------------------
def sensitivity_binary(y_true,y_pred):
    TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()
    print('\tFP:{},FN:{},TP:{},TN:{}'.format(FP,FN,TP,TN))
    Sensitivity=TP/(TP+FN)
    print("\tSensitivity: ",Sensitivity)
    return Sensitivity
#---------------------------------------------------------------------------------------------------
def sensitivity_multiclass(y_true,y_pred):
    cm=confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm)
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    print('\tFP:{},FN:{},TP:{},TN:{}'.format(FP,FN,TP,TN))
    Sensitivity = TP/(TP+FN)
    print("\tClass Wise Sensitivity: ",Sensitivity)
    Sensitivity_mean = np.mean(Sensitivity)
    print("\tMean Sensitivity: ",Sensitivity_mean)
    return Sensitivity,Sensitivity_mean
#---------------------------------------------------------------------------------------------------
def specificity_binary(y_true,y_pred,binary_label=False):
    TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()
    print('\tFP:{},FN:{},TP:{},TN:{}'.format(FP,FN,TP,TN))
    Specificity=TN/(TN+FP)
    print("\tSpecificity: ",Specificity)    
    return Specificity
#---------------------------------------------------------------------------------------------------
def specificity_multiclass(y_true,y_pred):
    cm=confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm)  
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    print('\tFP:{},FN:{},TP:{},TN:{}'.format(FP,FN,TP,TN))
    
    Specificity = TN/(TN+FP)
    print("\tClass Wise Specificity: ",Specificity)
    Specificity_mean = np.mean(Specificity)
    print("\tMean Specificity: ",Specificity_mean)
    return Specificity,Specificity_mean
#---------------------------------------------------------------------------------------------------
def precision_binary(y_true,y_pred,binary_label=False):
    TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()
    print('\tFP:{},FN:{},TP:{},TN:{}'.format(FP,FN,TP,TN))
    Precision = TP/(TP+FP)
    print("\tPrecision: ",Precision)    
    return Precision
#---------------------------------------------------------------------------------------------------
def precision_multiclass(y_true,y_pred):
    cm=confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm)  
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    print('\tFP:{},FN:{},TP:{},TN:{}'.format(FP,FN,TP,TN))
    
    Precision = TP/(TP+FP)
    print("\tClass Wise Precision: ",Precision)
    Precision_mean = np.mean(Precision)
    print("\tMean Precision: ",Precision)
    return Precision,Precision_mean
#---------------------------------------------------------------------------------------------------
def accuracy_confusion_matrix_precision_recall_multiclass(y_true,y_pred,title_prefix=None,target_names=None,savefig_path=None):
    if title_prefix != None:
        title_prefix = title_prefix.strip()
    else:
        title_prefix =''
    if len(title_prefix)>1:
        title_prefix = title_prefix+" "
    acc = accuracy_score(y_true,y_pred)
    print("\n"+title_prefix+"Accuracy : ",acc)
    conf_mat_fig_path, acc, confusion_matrix_value = plot_confusion_matrix(y_true,y_pred,target_names=target_names,savefig_path=savefig_path)
    sens,sens_mean = sensitivity_multiclass(y_true,y_pred)
    spec,spec_mean = specificity_multiclass(y_true,y_pred)
    prec,prec_mean = precision_multiclass(y_true,y_pred)
    #print("\t"+title_prefix+"Mean Sensitivity: ",sens_mean)
    #print("\t"+title_prefix+"Mean Specificity: ",spec_mean)
    #conf_mat_fig.savefig('/notebooks/EfficientNet_DR/models/20230301-122358/train_confusion_matrix_multiclass.jpg')
    return conf_mat_fig_path, acc, confusion_matrix_value, sens, sens_mean, spec,spec_mean,prec,prec_mean
#---------------------------------------------------------------------------------------------------
def accuracy_confusion_matrix_precision_recall_for_binary_label(y_true,y_pred,title_prefix=None,target_names=None,savefig_path=None):
    if title_prefix != None:
        title_prefix = title_prefix.strip()
    else:
        title_prefix =''
    if len(title_prefix)>1:
        title_prefix = title_prefix+" "
    print("\n"+title_prefix+"Accuracy : ",accuracy_score(y_true,y_pred))
    conf_mat_fig_path, acc, confusion_matrix_value = plot_confusion_matrix(y_true,y_pred,target_names=target_names,savefig_path=savefig_path)
    sens = sensitivity_binary(y_true,y_pred)
    spec = specificity_binary(y_true,y_pred)
    prec = precision_binary(y_true,y_pred)
    return conf_mat_fig_path, acc, confusion_matrix_value, sens, spec ,prec


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


# https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html

def multi_class_label_to_onehot_binaried(multi_class_label,number_of_class=5):
    """
    convert [4, 0, 2, 0, 3, 0]
    to  array([[0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0]])
    """
    label_binarize=[]

    for i, pred in enumerate(np.copy(multi_class_label)):
        temp = np.zeros((number_of_class),dtype=int)
        temp[pred] = 1
        label_binarize.append(temp)
    label_binarize = np.array(label_binarize)
    label_binarize
    return label_binarize
#---------------------------------------------------------------------------------------------------
def roc_plot_multiclass(y_ground_binarize,y_preds_binarized,n_classes,lw,title_prefix=""):
    #n_classes = 5
    #lw =2

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_ground_binarize[:, i], y_preds_binarized
    [:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(y_ground_binarize.ravel(), y_preds_binarized.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    # First aggregate all false positive rates
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

    # Then interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])

    # Finally average it and compute AUC
    mean_tpr /= n_classes

    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    # Plot all ROC curves
    plt.figure(figsize=(10,8))
    plt.plot(
        fpr["micro"],
        tpr["micro"],
        label="micro-average ROC curve (area = {0:0.2f})".format(roc_auc["micro"]),
        color="deeppink",
        linestyle=":",
        linewidth=4,
    )

    plt.plot(
        fpr["macro"],
        tpr["macro"],
        label="macro-average ROC curve (area = {0:0.2f})".format(roc_auc["macro"]),
        color="navy",
        linestyle=":",
        linewidth=4,
    )

    colors = cycle(["aqua", "darkorange", "cornflowerblue",'tab:olive','tab:cyan'])
    for i, color in zip(range(n_classes), colors):
        plt.plot(
            fpr[i],
            tpr[i],
            color=color,
            lw=lw,
            label="ROC curve of class {0} (area = {1:0.2f})".format(i, roc_auc[i]),
        )

    plt.plot([0, 1], [0, 1], "k--", lw=lw)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(str(title_prefix) +"ROC Curve")
    plt.legend(loc="lower right")
    plt.axis('tight') # to add padding
    return plt

#---------------------------------------------------------------------------------------------------
def roc_plot_binaryclass(y_grd_binary,y_preds_model_2_binary,title_prefix=""):
    fpr_binary, tpr_binary, thresh_binary = roc_curve(y_grd_binary,y_preds_model_2_binary, pos_label=1)

    # roc curve for tpr = fpr 
    random_probs = [0 for i in range(len(y_grd_binary))]
    p_fpr, p_tpr, _ = roc_curve(y_grd_binary, random_probs, pos_label=1)

    # auc scores
    auc_score1 = roc_auc_score(y_grd_binary, y_preds_model_2_binary)

    # plot roc curves
    plt.plot(fpr_binary, tpr_binary, linestyle='--',color='orange', label="AUC Score {0} (area = {1:0.2f})".format(1, auc_score1))
    plt.plot(p_fpr, p_tpr, linestyle='--', color='blue')
    # title
    plt.title(str(title_prefix) +"ROC Curve")
    # x label
    plt.xlabel('False Positive Rate')
    # y label
    plt.ylabel('True Positive rate')
    plt.axis('tight') # to add padding
    plt.legend(loc="lower right")
    return plt
#---------------------------------------------------------------------------------------------------