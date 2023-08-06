# -*- coding: UTF-8 -*-
"""
@Project ：work2_immune_subtype 
@File    ：w2-utils.py
@Author  ：LanHao
@Date    ：2023/4/28 15:32 
"""
import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def adj_normalization(adj_matrix):
    """
    按L=I-D^{-1/2} (A+I) D^{-1/2}对称规范化邻接矩阵，得到拉普拉斯矩阵
    :param adj_matrix:array格式的邻接矩阵
    :return:对称规范化后的拉普拉斯矩阵L
    """
    adj_hat = adj_matrix + np.eye(adj_matrix.shape[0])
    row_sum = np.array(adj_hat.sum(1))
    degree_mx_inverse_sqrt = np.diag(np.power(row_sum, -0.5).flatten())
    adj_normalized = adj_hat.dot(degree_mx_inverse_sqrt).transpose().dot(degree_mx_inverse_sqrt)
    return adj_normalized


def sparse_mx_to_torch_sparse_tensor(sparse_mx):
    """
    将scipy的稀疏矩阵转换为torch的稀疏张量
    :param sparse_mx: 需要转化的稀疏矩阵
    :return: torch sparse tensor格式的稀疏tensor，用于输入神经网络
    """

    return torch.FloatTensor(sparse_mx)


def load_data(ex, mut, alt):
    gene = pd.read_csv(ex, index_col=0).values.astype(float)
    smg = pd.read_csv(mut, index_col=0).values.astype(float)
    cna = pd.read_csv(alt, index_col=0).values.astype(float)

    smg = StandardScaler().fit_transform(smg)
    cna = StandardScaler().fit_transform(cna)
    gene = StandardScaler().fit_transform(gene)
    gene_ts = torch.Tensor(gene)
    smg_ts = torch.Tensor(smg)
    cna_ts = torch.Tensor(cna)

    return gene_ts, smg_ts, cna_ts


def get_sse(i, data):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit([x for x in data])
    return kmeans.inertia_


def calc_elbow(k, data):
    k_list = range(1, k)
    sse_list = [get_sse(a, data) for a in k_list]
    diff_list = np.diff(sse_list)
    diff2_list = np.diff(diff_list)
    return np.argmax(diff2_list) + 2


def kmeans_cluster(data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    labels = kmeans.fit_predict(data)
    s_score = silhouette_score(data, labels)
    return s_score
