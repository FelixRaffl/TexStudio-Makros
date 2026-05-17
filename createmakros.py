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

# 2. Define all static macros
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
            "\t\\includegraphics[width=0.7\\textwidth]{%|}",
            "\t\\caption{}",
            "\t\\label{fig:}",
            "\\end{figure}"
        ],
        "trigger": "@fig1"
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
            "\t\t\\includegraphics[height=\\textwidth]{%|}",
            "\t\\end{minipage}",
            "\t\\hfill",
            "\t\\begin{minipage}[t]{0.48\\textwidth}",
            "\t\t\\centering",
            "\t\t\\includegraphics[height=\\textwidth]{}",
            "\t\\end{minipage}",
            "\t\\caption[]{}",
            "\t\\label{fig:}",
            "\\end{figure}"
        ],
        "trigger": "@fig2"
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
            "\t\\begin{lstlisting}[caption={}, label={code:}]",
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
            "\\frac{%|}{}"
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
    "Derivative": {
        "abbrev": "",
        "description": "Fraction for derivatives using \\di",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Derivative",
        "shortcut": "",
        "tag": [
            "\\frac{\\di {}}{\\di {}}%|"
        ],
        "trigger": "@der"
    },
    "Time_Derivative": {
        "abbrev": "",
        "description": "Fraction for time derivatives using \\di",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Time Derivative",
        "shortcut": "",
        "tag": [
            "\\frac{\\di {}}{\\di t}%|"
        ],
        "trigger": "@tder"
    },
    "Partial_Derivative": {
        "abbrev": "",
        "description": "Fraction for partial derivatives",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Partial Derivative",
        "shortcut": "",
        "tag": [
            "\\frac{\\partial {}}{\\partial {}}%|"
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
            "\t\\label{eq:}",
            "\t%|",
            "\\end{equation}"
        ],
        "trigger": "@eq"
    },
    "Quantity": {
        "abbrev": "",
        "description": "siunitx quantity command",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Quantity",
        "shortcut": "",
        "tag": [
            "\\qty{%|}{}"
        ],
        "trigger": "@qty"
    },
    "Parentheses": {
        "abbrev": "",
        "description": "Auto-scaling parentheses",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Parentheses",
        "shortcut": "",
        "tag": [
            "\\left(%|\\right)"
        ],
        "trigger": "@par"
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
    },
    "Quad_Text": {
        "abbrev": "",
        "description": "Inserts text surrounded by quads",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Quad Text",
        "shortcut": "",
        "tag": [
            "\\quad \\text{%|} \\quad"
        ],
        "trigger": "@qat"
    },
    "Subscript": {
        "abbrev": "",
        "description": "Standard subscript",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Subscript",
        "shortcut": "",
        "tag": [
            "%|_{}"
        ],
        "trigger": "@sub"
    },
    "Math_Subscript": {
        "abbrev": "",
        "description": "Math mode subscript",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Math Subscript",
        "shortcut": "",
        "tag": [
            "$%|_{}$"
        ],
        "trigger": "@msub"
    }
}

# 3. Dynamically generate Tables for 1 to 6 columns
for i in range(1, 7):
    col_def = "l" * i  # Creates 'l', 'll', 'lll', etc.
    header_row = "\t" + " & ".join([""] * i) + " \\\\ \\hline"
    data_row = "\t%|" + (" & " * (i - 1)) + " \\\\"
    
    macros_data[f"Table_{i}Col"] = {
        "abbrev": "",
        "description": f"Standard Table with {i} Columns",
        "formatVersion": 1,
        "menu": "Custom",
        "name": f"Table {i} Columns",
        "shortcut": "",
        "tag": [
            "\\begin{table}[H]",
            "\t\\centering",
            "\t\\caption{}",
            "\t\\label{tab:}",
            "\t\\footnotesize ",
            f"\t\\begin{{tabular}}{{{col_def}}}",
            "\t\\hline",
            header_row,
            data_row,
            "\t\\hline",
            "\t\\end{tabular}",
            "\\end{table}"
        ],
        "trigger": f"@tab{i}"
    }

# 4. Create folder and clean up old files
folder_name = "Macros"
os.makedirs(folder_name, exist_ok=True)

# Delete existing .txsMacro files in the folder so only the new ones remain
print(f"Räume alten Ordner '{folder_name}' auf...")
for file in os.listdir(folder_name):
    if file.endswith(".txsMacro"):
        file_path = os.path.join(folder_name, file)
        os.remove(file_path)

# 5. Write the new files
for filename, file_content in macros_data.items():
    full_filename = os.path.join(folder_name, f"{filename}.txsMacro")
    
    with open(full_filename, "w", encoding="utf-8") as f:
        json.dump(file_content, f, indent=4)
        
    print(f"Erfolgreich erstellt: {full_filename}")

print(f"\nAlle Dateien wurden generiert und im Ordner '{folder_name}' gespeichert!")