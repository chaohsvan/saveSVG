import os
import datetime

def save_svg_by_trigger():
    print("--- SVG 快速粘贴工具 (单引号结尾触发) ---")
    
    while True:
        # 自动生成文件名
        filename = f"svg_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.svg"
        
        print("\n请粘贴 SVG 代码，并在最后加上 ' 或 ‘ 然后回车：")
        
        content_lines = []
        while True:
            try:
                line = input()
                # 检查当前行是否以 中文或英文单引号 结尾
                if line.endswith("'") or line.endswith("‘"):
                    # 去掉行尾的触发符
                    clean_line = line[:-1]
                    content_lines.append(clean_line)
                    break
                content_lines.append(line)
            except EOFError:
                break
    
        content = "\n".join(content_lines).strip()
        
        # 2. 检查内容
        if not content:
            print("\n❌ 未识别到有效内容。")
            continue  # 继续下一次循环

        # 3. 写入文件
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"\n✅ 识别到结束符，保存成功！")
            print(f"📍 路径: {os.path.abspath(filename)}")
        except Exception as e:
            print(f"❌ 写入失败: {e}")
            continue  # 继续下一次循环
        
        # 原有的步骤 4 (询问是否继续) 已被移除，代码将直接循环回到顶部等待下一个输入

if __name__ == "__main__":
    save_svg_by_trigger()
