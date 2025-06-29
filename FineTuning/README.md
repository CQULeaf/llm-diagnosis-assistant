# 大模型微调通用方法

本项目用于大语言模型（LLM）的微调，支持自定义数据集与模型路径配置。

## 目录结构

- `config.py`：配置文件，设置模型路径、数据集路径及相关参数。
- `datasetScissiors.py`：数据集处理脚本，用来。
- `fineTuning.ipynb`：微调流程 Jupyter Notebook 示例。
- `modelfile`：将模型导入ollama的配置文件
- `datasets/`：存放各类训练数据集（如 JSONL 格式）。

## 快速开始

1. **配置参数**  
   编辑 [`config.py`](config.py)，设置路径与数据集大小等参数。

2. **准备数据集**  
   将训练数据集放入 [`datasets/`](datasets/) 文件夹，支持 JSONL 格式。

3. **运行微调**  
   可直接运行 [`fineTuning.ipynb`](fineTuning.ipynb) 进行模型微调。

## 依赖环境
- Python 3.11+
- Pytorch 2.7.0+cu127
- Unsloth 2025.6.5
- llama.cpp
- ollama 0.9.3

### 关于llama.cpp如何build
[https://blog.csdn.net/spiderwower/article/details/138755776/](https://blog.csdn.net/spiderwower/article/details/138755776/)  
[https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)