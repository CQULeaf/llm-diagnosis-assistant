import json
import ijson

input_path = "datasets/QizhenDataset.json"
output_path = "datasets/QizhenDataset_2000.jsonl"
max_lines = 2000

with open(input_path, "r", encoding="utf-8") as fin:
    first_char = fin.read(1)
    fin.seek(0)
    if first_char == '[':
        # 流式处理超大json数组
        with open(output_path, "w", encoding="utf-8") as fout:
            for i, item in enumerate(ijson.items(fin, 'item')):
                if i >= max_lines:
                    break
                fout.write(json.dumps(item, ensure_ascii=False) + '\n')
    else:
        # 处理jsonl
        with open(output_path, "w", encoding="utf-8") as fout:
            for i, line in enumerate(fin):
                if i >= max_lines:
                    break
                fout.write(line)
print(f"已保存前{max_lines}条到 {output_path}")