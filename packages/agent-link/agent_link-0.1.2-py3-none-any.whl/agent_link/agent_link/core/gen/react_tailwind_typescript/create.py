import subprocess

def create_react_app_with_tailwind_typescript(project_dir):
    subprocess.run(["npx", "create-react-app", project_dir, "--template", "typescript"])
    subprocess.run(["npm", "install", "-D", "tailwindcss@latest", "postcss@latest", "autoprefixer@latest"], cwd=project_dir)
