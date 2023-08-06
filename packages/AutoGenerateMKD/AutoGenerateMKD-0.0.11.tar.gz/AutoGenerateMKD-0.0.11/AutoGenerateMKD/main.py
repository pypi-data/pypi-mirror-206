# @Author: E-NoR
# @Date:   2022-11-30 02:05:53
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-30 04:45:58
from argparse import ArgumentParser
from pathlib import Path


def copy_mkdocs(target_path: Path, project_name: str):
    mkdocs_yml = Path(__file__).resolve().parent.joinpath("mkdocs.yml")
    target_path = target_path.joinpath("mkdocs.yml")
    with target_path.open("w") as f1:
        with mkdocs_yml.open("r") as f2:
            content = f2.read().replace("SITE NAME HERE", project_name)
        f1.write(content)


def auto_gen_markdown(path: str):
    root_dir = Path(path)
    project_dir = root_dir
    project_name = project_dir.name
    if not root_dir.exists():
        raise FileNotFoundError(f"Path {path} not found")
        
    copy_mkdocs(root_dir.parent, project_name)
    doc_files_dir = root_dir.joinpath("docs")
    summary_path = root_dir.parent.joinpath("SUMMARY.md")
    doc_files_dir.mkdir(parents=True, exist_ok=True)
    


    with summary_path.open("w", encoding="utf8") as f2:
        for file_path in project_dir.rglob("*.py"):
            module_path = file_path.with_suffix("").as_posix().replace("/", ".")
            md_file_path = Path(str(doc_files_dir / file_path.with_suffix(".md")).replace(f"{project_name}/",""))
            md_file_path.parent.mkdir(parents=True, exist_ok=True)
            with md_file_path.open("w", encoding="utf8") as f:
                f.write(f"::: {module_path}")
                file_name = md_file_path.name.rstrip(".md")
                f2.write(f"* [{file_name}]({md_file_path.name})\n")
    md_content = f"""
    # {project_dir.name}

    Welcome to My Project -- {project_dir.name}!
        
    more style:
        Material for MkDocs: https://squidfunk.github.io/mkdocs-material/reference/admonitions/
    """
    index_md = Path(str(doc_files_dir / "index.md").replace(f"{project_name}/",""))
    with index_md.open("w", encoding="utf8") as f:
        f.write(md_content)
    print("done.")


def main():
    parser = ArgumentParser(description="Process a project_path.")
    parser.add_argument("-p", "--project_path", dest="project_path", required=True, help="path of the project")
    args = parser.parse_args()

    project_path = args.project_path
    print(f"project_path: {project_path}")
    auto_gen_markdown(project_path)


if __name__ == "__main__":
    main()
