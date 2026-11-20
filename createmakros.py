import json
import os

# Get the exact directory where this Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Read the usepackages.tex file dynamically from the script's directory
packages_file = os.path.join(script_dir, "usepackages.tex")
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
    "Python_Code_Listing": {
        "abbrev": "",
        "description": "Python code snippet in centered minipage",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Python Code Listing",
        "shortcut": "",
        "tag": [
            "\\begin{center}",
            "\t\\begin{minipage}{0.9\\linewidth}",
            "\t\\begin{lstlisting}[language=Python, caption={}, label={code:}]",
            "\t%|",
            "\t\\end{lstlisting}",
            "\t\\end{minipage}",
            "\\end{center}"
        ],
        "trigger": "@pycode"
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
    },
    "PGF_Plot": {
        "abbrev": "",
        "description": "General pgfplots template",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "PGF Plot",
        "shortcut": "",
        "tag": [
            "\\begin{figure}[H]",
            "\t\\centering",
            "\t% --- Start the Axis Environment ---",
            "\t\\begin{axis}[",
            "\t\t% 1. General Appearance",
            "\t\twidth=12cm,                % Width of the plot",
            "\t\theight=8cm,                % Height of the plot",
            "\t\ttitle={%|General Plot Template}, % Main title",
            "\t\t",
            "\t\t% 2. Axis Labels",
            "\t\txlabel={X-axis Label (Units)}, ",
            "\t\tylabel={Y-axis Label (Units)},",
            "\t\t",
            "\t\t% 3. Axis Limits (Uncomment to force specific boundaries)",
            "\t\t% xmin=0, xmax=10,",
            "\t\t% ymin=-2, ymax=4,",
            "\t\t",
            "\t\t% 4. Grid Lines",
            "\t\tgrid=major,                    % Options: none, major, both",
            "\t\tgrid style={dashed, gray!50}, % Customize grid appearance",
            "\t\t",
            "\t\t% 5. Legend Position",
            "\t\tlegend pos=north west,        % Options: north/south east/west, outer north east",
            "\t\tlegend cell align={left},     % Aligns legend text to the left",
            "\t\t",
            "\t\t% 6. Tick Marks (Uncomment to customize the numbers on the axes)",
            "\t\t% xtick={0, 2, 4, 6, 8, 10},",
            "\t\t% ytick={-2, 0, 2, 4},",
            "\t]",
            "\t",
            "\t% --- Plot Type A: Mathematical Function ---",
            "\t\\addplot[",
            "\t\tcolor=blue,",
            "\t\tthick,",
            "\t\tdomain=0:10,       % Range of x values to calculate",
            "\t\tsamples=100        % Number of points to calculate (higher = smoother curve)",
            "\t]",
            "\t{sin(deg(x*1.5)) + 1}; % The function. Note: trig functions expect degrees by default",
            "\t\\addlegendentry{Math Function}",
            "\t",
            "\t% --- Plot Type B: Inline Coordinates ---",
            "\t\\addplot[",
            "\t\tcolor=red,",
            "\t\tthick,",
            "\t\tdashed,            % Line style (solid, dashed, dotted)",
            "\t\tmark=*,            % Marker style (*, o, x, square, triangle, etc.)",
            "\t\tmark size=2pt      % Adjust marker size",
            "\t]",
            "\tcoordinates {",
            "\t\t(0,0) (2,1.5) (4,0.5) (6,2.5) (8,1.2) (10,3.5)",
            "\t};",
            "\t\\addlegendentry{Coordinate Data}",
            "\t",
            "\t% --- Plot Type C: From a File (Commented out for the template) ---",
            "\t% \\addplot[",
            "\t%     color=darkgray, ",
            "\t%     thick",
            "\t% ] table [",
            "\t%     col sep=comma, ",
            "\t%     x=time, ",
            "\t%     y=velocity",
            "\t% ] {data.csv};",
            "\t% \\addlegendentry{CSV File Data}",
            "\t",
            "\t\\end{axis}",
            "\\end{figure}"
        ],
        "trigger": "@plot"
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

# 4. Create folder and clean up old files in the script's directory
folder_path = os.path.join(script_dir, "Macros")
os.makedirs(folder_path, exist_ok=True)

# Delete existing .txsMacro files in the folder so only the new ones remain
print(f"Räume alten Ordner '{folder_path}' auf...")
for file in os.listdir(folder_path):
    if file.endswith(".txsMacro"):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)

# 5. Write the new files
for filename, file_content in macros_data.items():
    full_filename = os.path.join(folder_path, f"{filename}.txsMacro")
    
    with open(full_filename, "w", encoding="utf-8") as f:
        json.dump(file_content, f, indent=4)
        
    print(f"Erfolgreich erstellt: {full_filename}")

print(f"\nAlle Dateien wurden generiert und im Ordner '{folder_path}' gespeichert!")