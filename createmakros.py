import json
import os

# 1. Read the usepackages.tex file dynamically
packages_file = "usepackages.tex"
packages_tag = []

try:
    with open(packages_file, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:  # Ignore empty lines
                packages_tag.append(clean_line)
    
    # Add the cursor drop at the very end
    packages_tag.append("%|")

except FileNotFoundError:
    # Fallback just in case the file is missing
    packages_tag = [
        "% ERROR: usepackages.tex not found!",
        "% Please make sure the file is in the same folder as this Python script.",
        "%|"
    ]

# 2. Define all macros (including the new dynamic one)
macros_data = {
    "Figure": {
        "abbrev": "",
        "description": "Standard Figure",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Figure",
        "shortcut": "",
        "tag": [
            "\\begin{figure}[H]",
            "\t\\centering",
            "\t\\includegraphics[width=%<1\\textwidth%>]{%<Grafiken/pfad.pdf%>}",
            "\t\\caption{%<Caption%>}",
            "\t\\label{fig:%<label%>}",
            "\\end{figure}",
            "%|"
        ],
        "trigger": "@fig"
    },
    "Table": {
        "abbrev": "",
        "description": "Standard Table with footnotesize",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Table",
        "shortcut": "",
        "tag": [
            "\\begin{table}[H]",
            "\t\\centering",
            "\t\\caption{%<Caption%>}",
            "\t\\label{tab:%<label%>}",
            "\t\\footnotesize ",
            "\t\\begin{tabular}{%<ll%>}",
            "\t\\hline",
            "\t%<Header 1%> & %<Header 2%> \\\\ \\hline",
            "\t%| & \\\\",
            "\t\\hline",
            "\t\\end{tabular}",
            "\\end{table}"
        ],
        "trigger": "@tab"
    },
    "Double_Figure": {
        "abbrev": "",
        "description": "Two Side-by-Side Figures with Minipages",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Double Figure",
        "shortcut": "",
        "tag": [
            "\\begin{figure}[H]",
            "\t\\centering",
            "\t\\begin{minipage}[t]{0.48\\textwidth}",
            "\t\t\\centering",
            "\t\t\\includegraphics[height=\\textwidth]{%<Grafiken/pfad1.pdf%>}",
            "\t\\end{minipage}",
            "\t\\hfill",
            "\t\\begin{minipage}[t]{0.48\\textwidth}",
            "\t\t\\centering",
            "\t\t\\includegraphics[height=\\textwidth]{%<Grafiken/pfad2.pdf%>}",
            "\t\\end{minipage}",
            "\t\\caption[%<Kurzes Caption für Verzeichnis%>]{%<Langes Caption%>}",
            "\t\\label{fig:%<label%>}",
            "\\end{figure}",
            "%|"
        ],
        "trigger": "@doublefig"
    },
    "Code_Listing": {
        "abbrev": "",
        "description": "Code snippet in centered minipage",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Code Listing",
        "shortcut": "",
        "tag": [
            "\\begin{center}",
            "\t\\begin{minipage}{0.9\\linewidth}",
            "\t\\begin{lstlisting}[caption={%<Caption%>}, label={code:%<label%>}]",
            "\t%|",
            "\t\\end{lstlisting}",
            "\t\\end{minipage}",
            "\\end{center}"
        ],
        "trigger": "@code"
    },
    "Fraction": {
        "abbrev": "",
        "description": "Standard mathematical fraction",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Fraction",
        "shortcut": "",
        "tag": [
            "\\frac{%<%>}{%<%>}%|"
        ],
        "trigger": "@frac"
    },
    "Itemize": {
        "abbrev": "",
        "description": "Itemize list environment",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Itemize",
        "shortcut": "",
        "tag": [
            "\\begin{itemize}",
            "\t\\item %|",
            "\\end{itemize}"
        ],
        "trigger": "@item"
    },
    "Partial_Derivative": {
        "abbrev": "",
        "description": "Fraction for partial derivatives",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Partial Derivative",
        "shortcut": "",
        "tag": [
            "\\frac{\\partial %<%>}{\\partial %<%>}%|"
        ],
        "trigger": "@pder"
    },
    "Equation": {
        "abbrev": "",
        "description": "Standard Equation Environment with Label",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Equation",
        "shortcut": "",
        "tag": [
            "\\begin{equation}",
            "\t\\label{eq:%<label%>}",
            "\t%|",
            "\\end{equation}"
        ],
        "trigger": "@eq"
    },
    "Packages": {
        "abbrev": "",
        "description": "Auto-inserts packages from usepackages.tex",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Insert Packages",
        "shortcut": "",
        "tag": packages_tag,
        "trigger": "@pkg"
    }
}

# 3. Create folder and files
folder_name = "Macros"
os.makedirs(folder_name, exist_ok=True)

for filename, file_content in macros_data.items():
    full_filename = os.path.join(folder_name, f"{filename}.txsMacro")
    
    with open(full_filename, "w", encoding="utf-8") as f:
        json.dump(file_content, f, indent=4)
        
    print(f"Erfolgreich erstellt: {full_filename}")

print(f"\nAlle Dateien wurden generiert und im Ordner '{folder_name}' gespeichert!")