import tkinter as tk
import math
import json
import os
from datetime import datetime

# #region agent log
def _log(hypothesis_id, location, message, data=None):
    try:
        log_dir = r"c:\Users\user\OneDrive\Desktop\Python Projects\.cursor"
        log_path = os.path.join(log_dir, "debug.log")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        log_entry = {
            "timestamp": int(datetime.now().timestamp() * 1000),
            "location": location,
            "message": message,
            "data": data or {},
            "sessionId": "debug-session",
            "runId": "run1",
            "hypothesisId": hypothesis_id
        }
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        # Fallback: print to stderr if logging fails
        import sys
        print(f"LOG_ERROR: {e}", file=sys.stderr)
# #endregion


class ScientificCalculator:
    def __init__(self, root):
        # #region agent log
        _log("H3", "calculator.py:7", "__init__ entry", {"root_type": str(type(root))})
        # #endregion
        try:
            self.root = root
            # #region agent log
            _log("H3", "calculator.py:10", "root assigned")
            # #endregion
            self.root.title("Scientific Calculator")
            # #region agent log
            _log("H3", "calculator.py:12", "title set")
            # #endregion
            self.root.geometry("600x650")
            # #region agent log
            _log("H3", "calculator.py:14", "geometry set")
            # #endregion
            self.root.resizable(False, False)
            # #region agent log
            _log("H3", "calculator.py:16", "resizable set")
            # #endregion
            self.root.configure(bg='#1a1a1a')  # Deep dark background
            # #region agent log
            _log("H3", "calculator.py:18", "background configured")
            # #endregion
            
            # Current expression being built
            self.expression = ""
            # Display variable
            self.display_var = tk.StringVar()
            self.display_var.set("0")
            # #region agent log
            _log("H3", "calculator.py:25", "variables initialized")
            # #endregion
            
            # Create GUI components
            # #region agent log
            _log("H3", "calculator.py:28", "calling create_widgets")
            # #endregion
            self.create_widgets()
            # #region agent log
            _log("H3", "calculator.py:30", "__init__ completed successfully")
            # #endregion
        except Exception as e:
            # #region agent log
            _log("H3", "calculator.py:32", "__init__ exception", {"error": str(e), "type": str(type(e))})
            # #endregion
            raise
        
    def create_widgets(self):
        # #region agent log
        _log("H4", "calculator.py:22", "create_widgets entry")
        # #endregion
        try:
            # Display screen with modern dark styling
            # #region agent log
            _log("H4", "calculator.py:25", "creating display_frame")
            # #endregion
            display_frame = tk.Frame(self.root, bg='#1a1a1a')
            # #region agent log
            _log("H4", "calculator.py:27", "display_frame created")
            # #endregion
            # #region agent log
            _log("H2", "calculator.py:28", "creating Entry widget with font", {"font": "Segoe UI"})
            # #endregion
            display = tk.Entry(
                display_frame,
                textvariable=self.display_var,
                font=('Segoe UI', 28, 'bold'),
                bg='#0d0d0d',
                fg='#00ff88',
                justify='right',
                bd=0,
                insertwidth=0,
                state='readonly',
                readonlybackground='#0d0d0d',
                relief='flat'
            )
            # #region agent log
            _log("H4", "calculator.py:42", "Entry widget created")
            # #endregion
            display.pack(fill='both', expand=True, padx=8, pady=8)
            # #region agent log
            _log("H4", "calculator.py:44", "display packed")
            # #endregion
            display_frame.pack(fill='both', expand=True, padx=10, pady=(10, 5))
            # #region agent log
            _log("H4", "calculator.py:46", "display_frame packed")
            # #endregion
        except Exception as e:
            # #region agent log
            _log("H2", "calculator.py:48", "display creation exception", {"error": str(e), "type": str(type(e))})
            # #endregion
            # #region agent log
            _log("H4", "calculator.py:50", "display creation exception", {"error": str(e), "type": str(type(e))})
            # #endregion
            raise
        
        # Button frame
        # #region agent log
        _log("H4", "calculator.py:50", "creating button_frame")
        # #endregion
        button_frame = tk.Frame(self.root, bg='#1a1a1a')
        button_frame.pack(fill='both', expand=True, padx=10, pady=5)
        # #region agent log
        _log("H4", "calculator.py:53", "button_frame created and packed")
        # #endregion
        
        # Button configuration with modern styling
        # #region agent log
        _log("H2", "calculator.py:56", "setting button font", {"font": "Segoe UI"})
        # #endregion
        button_config = {
            'font': ('Segoe UI', 13, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'width': 9,
            'height': 2,
            'cursor': 'hand2',
            'activebackground': '#2a2a2a'
        }
        # #region agent log
        _log("H4", "calculator.py:65", "button_config created")
        # #endregion
        
        # Modern Dark Theme Color Palette
        # Scientific functions - Dark gray-blue
        sci_color = {'bg': '#2d3748', 'fg': '#a0aec0', 'activebackground': '#3d4758'}
        # Advanced operations - Darker gray
        adv_color = {'bg': '#2d3748', 'fg': '#cbd5e0', 'activebackground': '#3d4758'}
        # Numbers - Medium dark gray
        num_color = {'bg': '#4a5568', 'fg': '#ffffff', 'activebackground': '#5a6578'}
        # Operations - Orange accent
        op_color = {'bg': '#ff6b35', 'fg': '#ffffff', 'activebackground': '#ff8c5a'}
        # Clear/Delete - Red accent
        clear_color = {'bg': '#e53e3e', 'fg': '#ffffff', 'activebackground': '#fc8181'}
        # Equals - Green accent
        equals_color = {'bg': '#38a169', 'fg': '#ffffff', 'activebackground': '#48bb78'}
        
        # First row - Scientific functions
        row1_buttons = [
            ('sin', self.button_click, sci_color),
            ('cos', self.button_click, sci_color),
            ('tan', self.button_click, sci_color),
            ('asin', self.button_click, sci_color),
            ('acos', self.button_click, sci_color),
            ('atan', self.button_click, sci_color),
        ]
        
        # Second row - More scientific functions
        row2_buttons = [
            ('log', self.button_click, sci_color),
            ('ln', self.button_click, sci_color),
            ('√', self.button_click, adv_color),
            ('x²', self.button_click, adv_color),
            ('x^y', self.button_click, adv_color),
            ('%', self.button_click, adv_color),
        ]
        
        # Third row - Parentheses and operations
        row3_buttons = [
            ('(', self.button_click, sci_color),
            (')', self.button_click, sci_color),
            ('÷', self.button_click, op_color),
            ('×', self.button_click, op_color),
            ('-', self.button_click, op_color),
            ('+', self.button_click, op_color),
        ]
        
        # Fourth row - Control and equals
        row4_buttons = [
            ('AC', self.clear_all, clear_color),
            ('DEL', self.delete_last, clear_color),
            ('=', self.calculate, equals_color),
        ]
        
        # Bottom row - All numbers horizontally (0-9 and decimal)
        row5_buttons = [
            ('0', self.button_click, num_color),
            ('1', self.button_click, num_color),
            ('2', self.button_click, num_color),
            ('3', self.button_click, num_color),
            ('4', self.button_click, num_color),
            ('5', self.button_click, num_color),
            ('6', self.button_click, num_color),
            ('7', self.button_click, num_color),
            ('8', self.button_click, num_color),
            ('9', self.button_click, num_color),
            ('.', self.button_click, num_color),
        ]
        
        # Create buttons
        rows = [
            row1_buttons,
            row2_buttons,
            row3_buttons,
            row4_buttons,
            row5_buttons,
        ]
        
        # #region agent log
        _log("H4", "calculator.py:131", "starting button creation loop", {"num_rows": len(rows)})
        # #endregion
        for row_idx, row_buttons in enumerate(rows):
            # #region agent log
            _log("H4", "calculator.py:133", "processing row", {"row_idx": row_idx, "num_buttons": len(row_buttons)})
            # #endregion
            for col_idx, (text, command, style) in enumerate(row_buttons):
                # #region agent log
                _log("H5", "calculator.py:135", "creating button", {"text": text, "row": row_idx, "col": col_idx})
                # #endregion
                try:
                    # Create a closure to properly capture text and command
                    if command == self.clear_all:
                        btn_command = lambda cmd=self.clear_all: cmd()
                    elif command == self.delete_last:
                        btn_command = lambda cmd=self.delete_last: cmd()
                    elif command == self.calculate:
                        btn_command = lambda cmd=self.calculate: cmd()
                    else:
                        btn_command = lambda t=text, cmd=self.button_click: cmd(t)
                    # #region agent log
                    _log("H5", "calculator.py:145", "lambda created", {"text": text})
                    # #endregion
                    
                    btn = tk.Button(
                        button_frame,
                        text=text,
                        command=btn_command,
                        **{**button_config, **style}
                    )
                    # #region agent log
                    _log("H5", "calculator.py:153", "Button widget created", {"text": text})
                    # #endregion
                    btn.grid(row=row_idx, column=col_idx, padx=3, pady=3, sticky='nsew')
                    # #region agent log
                    _log("H5", "calculator.py:155", "Button gridded", {"text": text})
                    # #endregion
                except Exception as e:
                    # #region agent log
                    _log("H5", "calculator.py:157", "button creation exception", {"text": text, "error": str(e), "type": str(type(e))})
                    # #endregion
                    raise
        
        # Configure grid weights - adjust for new layout
        # Find max columns needed
        # #region agent log
        _log("H4", "calculator.py:160", "configuring grid weights")
        # #endregion
        try:
            max_cols = max(len(row) for row in rows)
            # #region agent log
            _log("H4", "calculator.py:163", "max_cols calculated", {"max_cols": max_cols})
            # #endregion
            for i in range(max_cols):
                button_frame.grid_columnconfigure(i, weight=1)
            for i in range(len(rows)):
                button_frame.grid_rowconfigure(i, weight=1)
            # #region agent log
            _log("H4", "calculator.py:168", "grid weights configured")
            # #endregion
        except Exception as e:
            # #region agent log
            _log("H4", "calculator.py:170", "grid config exception", {"error": str(e), "type": str(type(e))})
            # #endregion
            raise
        # #region agent log
        _log("H4", "calculator.py:172", "create_widgets completed successfully")
        # #endregion
    
    def button_click(self, char):
        """Handle button clicks for building expressions"""
        if self.expression == "0" or self.display_var.get().startswith("Error"):
            self.expression = ""
            self.display_var.set("")
        
        # Handle special functions
        if char in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln']:
            self.expression += f"{char}("
        elif char == '√':
            self.expression += "sqrt("
        elif char == 'x²':
            self.expression += "**2"
        elif char == 'x^y':
            self.expression += "**"
        elif char == '%':
            self.expression += "%"  # Fixed: modulo operator instead of /100
        elif char == '×':
            self.expression += "*"
        elif char == '÷':
            self.expression += "/"
        else:
            self.expression += char
        
        self.display_var.set(self.expression)
    
    def clear_all(self, char=None):
        """Clear all input"""
        self.expression = ""
        self.display_var.set("0")
    
    def delete_last(self, char=None):
        """Delete last character"""
        if self.display_var.get().startswith("Error"):
            self.clear_all()
            return
        
        if len(self.expression) > 0:
            self.expression = self.expression[:-1]
            if len(self.expression) == 0:
                self.display_var.set("0")
            else:
                self.display_var.set(self.expression)
        else:
            self.display_var.set("0")
    
    def calculate(self, char=None):
        """Evaluate the expression"""
        try:
            if not self.expression:
                return
            
            # Replace display symbols with Python operators
            expression = self.expression.replace('×', '*').replace('÷', '/')
            
            # Define safe math functions
            safe_dict = {
                'sqrt': math.sqrt,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'asin': math.asin,
                'acos': math.acos,
                'atan': math.atan,
                'log': math.log10,
                'ln': math.log,
                'pi': math.pi,
                'e': math.e,
                'pow': pow,
                '__builtins__': {}
            }
            
            # Evaluate the expression
            result = eval(expression, {"__builtins__": {}}, safe_dict)
            
            # Format result
            if isinstance(result, (int, float)):
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 10)
                
                self.display_var.set(str(result))
                self.expression = str(result)
            else:
                raise ValueError("Invalid result")
                
        except ZeroDivisionError:
            self.display_var.set("Error: Division by zero")
            self.expression = ""
        except (ValueError, SyntaxError, TypeError, NameError) as e:
            self.display_var.set("Error")
            self.expression = ""
        except Exception as e:
            self.display_var.set("Error")
            self.expression = ""


def main():
    # #region agent log
    _log("H1", "calculator.py:257", "main() entry")
    # #endregion
    try:
        # #region agent log
        _log("H1", "calculator.py:260", "creating Tk root")
        # #endregion
        root = tk.Tk()
        # #region agent log
        _log("H1", "calculator.py:262", "Tk root created", {"root_type": str(type(root))})
        # #endregion
        # #region agent log
        _log("H6", "calculator.py:264", "creating ScientificCalculator instance")
        # #endregion
        app = ScientificCalculator(root)
        # #region agent log
        _log("H6", "calculator.py:266", "ScientificCalculator instance created")
        # #endregion
        # #region agent log
        _log("H1", "calculator.py:268", "starting mainloop")
        # #endregion
        root.mainloop()
        # #region agent log
        _log("H1", "calculator.py:270", "mainloop exited")
        # #endregion
    except Exception as e:
        # #region agent log
        _log("H1", "calculator.py:272", "main() exception", {"error": str(e), "type": str(type(e))})
        # #endregion
        # #region agent log
        _log("H6", "calculator.py:274", "main() exception", {"error": str(e), "type": str(type(e))})
        # #endregion
        raise


if __name__ == "__main__":
    # #region agent log
    _log("H1", "calculator.py:263", "script entry point", {"__name__": __name__})
    # #endregion
    try:
        main()
    except Exception as e:
        # #region agent log
        _log("H1", "calculator.py:267", "top-level exception", {"error": str(e), "type": str(type(e))})
        # #endregion
        import sys
        import traceback
        print(f"ERROR: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        raise
