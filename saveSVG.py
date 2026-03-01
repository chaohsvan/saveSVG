import os

def save_svg_by_trigger():
    print("--- SVG 快速粘贴工具 (单引号结尾触发) ---")
    
    # 1. 文件命名
    name_input = input("1. 请输入文件名 (默认 'output'): ").strip() or "output"
    filename = name_input if name_input.lower().endswith('.svg') else f"{name_input}.svg"
    
    print(f"\n2. 请粘贴 SVG 代码，并在最后加上 ' 或 ‘ 然后回车：")
    print("--------------------------------------------------")
    print("示例粘贴内容：<svg>...</svg>'")
    print("--------------------------------------------------")
    
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
        return

    # 3. 写入文件
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✅ 识别到结束符，保存成功！")
        print(f"📍 路径: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"❌ 写入失败: {e}")

if __name__ == "__main__":
    save_svg_by_trigger()
