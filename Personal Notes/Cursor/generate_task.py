import os
from datetime import datetime

TEMPLATE_DIR = "./templates"
TASK_DIR = "./tasks"

def load_template(template_name):
    template_path = os.path.join(TEMPLATE_DIR, template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"模板文件不存在：{template_path}")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_task_file(task_name, template_name="default_template.md"):
    content = load_template(template_name)
    rendered = content.replace("{{task_name}}", task_name)
    
    task_file = os.path.join(TASK_DIR, f"{task_name}.md")
    os.makedirs(TASK_DIR, exist_ok=True)
    with open(task_file, "w", encoding="utf-8") as f:
        f.write(rendered)
    
    print(f"✅ 任务模板已生成：{task_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="任务模板生成器")
    parser.add_argument("--task", required=True, help="任务名称（用于文件名）")
    parser.add_argument("--template", default="default_template.md", help="模板文件名")

    args = parser.parse_args()
    generate_task_file(task_name=args.task, template_name=args.template)
