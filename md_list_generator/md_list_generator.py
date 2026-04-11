from pathlib import Path
'''
放根目錄，抓所有MD名單
'''

ROOT_FOLDER = Path.cwd()
#過濾名單
IGNORE_LIST = {'.gitignore', '__pycache__', '.git','README.md'}

class folder_operation:
    def __init__(self):
        pass
    
    def run(self):
        self._get_categories()

    def _should_ignore(self,path):
 

        #把路徑拆開過濾
        for part in path.parts:
            if part in IGNORE_LIST:
                return True
            
            #模糊匹配
            if path.name.startswith('.'):
                return True
        


    def _get_categories(self):
        root = ROOT_FOLDER
        output_file = ROOT_FOLDER / "output.txt"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        for path in sorted(root.rglob('*.md')):
            
            if path.name in IGNORE_LIST:
                continue
            if self._should_ignore(path):
                continue

            rel_path = path.relative_to(ROOT_FOLDER)
            with open(output_file,"a",encoding="utf-8") as f:
                f.write(str(rel_path) + "\n")

        

class text_editting:
    
    def __init__(self):
        self.data = ROOT_FOLDER / 'output.txt'

    def format_to_markdown(self):

        structured_data = []
        with self.data.open(encoding='utf-8') as f :
            for line in f:
                clean_path = line.strip() # 刪除換行符  
                if not clean_path: # split() 處理換行，會產生""，空字串在python是  False
                    continue
                p = Path(clean_path)  
                structured_data.append(f'- [{p.stem}]({p.as_posix()})')

        self.data.write_text("\n".join(structured_data) + "\n", encoding="utf-8")
        
        print(f"✅ {self.data.name} 已直接改寫完成！")

if __name__ == "__main__":
    fo =folder_operation()
    fo.run()
    te= text_editting()
    te.format_to_markdown()
