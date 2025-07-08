from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer, GenerationConfig
from peft import PeftModel
import os
import torch

# 载入预训练模型
base_model = "D:\Downloads\model\Qwen\Qwen3-0___6B"
config_kwargs= ""
tokenizer = AutoTokenizer.from_pretrained(base_model, use_fast=True, padding_side="left", **config_kwargs)
print("Tokenizer Load Success!")
config = AutoConfig.from_pretrained(base_model, **config_kwargs)
# Load and prepare pretrained models (without valuehead).
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    config=config,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    trust_remote_code=True,
    revision='main'
)
print('origin config =', model.config)
# 模型合并
ckpt_list = ["checkpoint-1000", "checkpoint-2000", "checkpoint-3000"]
for checkpoint in ckpt_list:
    print('Merge checkpoint: {}'.format(checkpoint))
    model = PeftModel.from_pretrained(model, os.path.join(lora_model, checkpoint))
    model = model.merge_and_unload()
print('merge config =', model.config)