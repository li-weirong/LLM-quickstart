from typing import Union
from pathlib import Path
import json


def advertise_gen_convert(data_dir: Union[str, Path], save_dir: Union[str, Path]):
    def _convert(in_file: Path, out_file: Path):
        with open(in_file, encoding='utf-8') as fin, open(out_file, 'w', encoding='utf-8') as fout:
            for line in fin:
                item = json.loads(line)
                sample = {'conversations': [{'role': 'user', 'content': item['content']},
                                       {'role': 'assistant', 'content': item['summary']}]}
                fout.write(json.dumps(sample, ensure_ascii=False) + '\n')

    data_dir = Path(data_dir).resolve()
    save_dir = Path(save_dir).resolve()

    for file_name in ['train.json', 'dev.json']:
        in_file = data_dir / file_name
        out_file = save_dir / f'{in_file.stem}.json'

        if in_file.is_file():
            out_file.parent.mkdir(parents=True, exist_ok=True)
            _convert(in_file, out_file)


advertise_gen_convert(data_dir="AdvertiseGen", save_dir="AdvertiseGen_Formatted")