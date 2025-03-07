import pymupdf4llm as mu4llm
import pathlib


def parse_md(input_file, output_file):

    input_path = pathlib.Path(input_file)
    md_text = mu4llm.to_markdown(input_path)

    output_path = pathlib.Path(output_file)

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(md_text)
    
    return output_path

if __name__ == "__main__":
    input_file = "testing_data/test.pdf"
    o_file = "testing_data/test_doc.md"

    try:
        result = parse_md(input_file, o_file)
        print(f"""File has been converted to markdown and saved at {result}""")
    except Exception as e:
        print(e)
        print("Error in parsing the file")