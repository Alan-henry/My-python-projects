import subprocess

def ppt_to_pdf(input_file, output_dir="."):
    subprocess.run([
        "soffice", "--headless", "--convert-to", "pdf",
        input_file, "--outdir", output_dir
    ])

ppt_to_pdf("presentation.pptx", "C:/output")
