import os
import pandas as pd
from fpdf import FPDF

# Make sure DejaVuSans.ttf is in the same directory as this script.
FONT_FILE = os.path.join(os.path.dirname(__file__), 'DejaVuSans.ttf')
FONT_FAMILY = 'DejaVuSans'

class WorkshopPDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Register regular and bold styles using the same TTF file
        self.add_font(FONT_FAMILY, '', FONT_FILE, uni=True)
        self.add_font(FONT_FAMILY, 'B', FONT_FILE, uni=True)
        self.set_auto_page_break(True, margin=15)

    def header(self):
        self.set_font(FONT_FAMILY, 'B', 16)
        self.set_text_color(30, 60, 150)
        self.cell(0, 10, 'Workshop Schedule', ln=True, align='C')
        self.set_text_color(0, 0, 0)
        # Add light gray horizontal line
        self.set_draw_color(200, 200, 200)  # Light gray
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def add_separator(self):
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.2)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def add_day_title(self, title):
        self.set_font(FONT_FAMILY, 'B', 14)
        self.set_text_color(40, 100, 200)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)
        self.ln(2)
        self.add_separator()

    def add_session(self, time, title, chair=None):
        self.add_separator()
        self.set_font(FONT_FAMILY, 'B', 12)
        text = f"{title} ({time})"
        self.set_text_color(20, 70, 160)
        self.multi_cell(0, 8, text)
        self.set_text_color(0, 0, 0)
        if chair:
            self.set_x(15)
            self.set_font(FONT_FAMILY, '', 11)
            self.cell(0, 7, f"Chair: {chair}", ln=True)
        self.ln(1)

    def add_speakers(self, speakers):
        for name, affiliation, topic in speakers:
            self.set_x(15)
            self.set_font(FONT_FAMILY, 'B', 11)
            self.set_text_color(50, 50, 50)
            self.cell(0, 6, f"{name} ({affiliation})", ln=True)
            self.set_text_color(0, 0, 0)
            self.set_x(20)
            self.set_font(FONT_FAMILY, '', 11)
            self.cell(0, 6, f"- {topic}", ln=True)
            self.ln(1)
        self.ln(1)

    def footer(self):
        self.set_y(-15)
        self.set_font(FONT_FAMILY, '', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

class AbstractPDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_font(FONT_FAMILY, '', FONT_FILE, uni=True)
        self.add_font(FONT_FAMILY, 'B', FONT_FILE, uni=True)
        self.set_auto_page_break(True, margin=15)

    def header(self):
        self.set_font(FONT_FAMILY, 'B', 16)
        self.set_text_color(30, 60, 150)
        self.cell(0, 10, 'Workshop Abstracts', ln=True, align='C')
        self.set_text_color(0, 0, 0)
        self.set_draw_color(200, 200, 200)  # Light gray
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def add_separator(self):
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.2)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def add_day_title(self, title):
        self.set_font(FONT_FAMILY, 'B', 14)
        self.set_text_color(40, 100, 200)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)
        self.ln(2)
        self.add_separator()

    def add_session_title(self, sess_num, sess_title, chair=None, time=None):
        self.add_separator()
        self.set_font(FONT_FAMILY, 'B', 12)
        line = f"Session {sess_num} - {sess_title}"
        if time:
            line += f" ({time})"
        self.set_text_color(20, 70, 160)
        self.multi_cell(0, 8, line)
        self.set_text_color(0, 0, 0)
        if chair:
            self.set_x(15)
            self.set_font(FONT_FAMILY, '', 11)
            self.cell(0, 7, f"Chair: {chair}", ln=True)
        self.ln(1)

    def add_abstract(self, name, affiliation, topic, abstract):
        self.set_x(15)
        self.set_font(FONT_FAMILY, 'B', 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 6, f"{name} ({affiliation})", ln=True)
        self.set_text_color(0, 0, 0)
        self.set_x(20)
        self.set_font(FONT_FAMILY, '', 11)
        self.cell(0, 6, f"- {topic}", ln=True)
        self.ln(1)
        self.set_x(20)
        self.set_font(FONT_FAMILY, '', 10)
        self.multi_cell(0, 5, f"Abstract: {abstract}")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font(FONT_FAMILY, '', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')


def generate_workshop_pdf(csv_path: str, output_path: str):
    # Read schedule CSV with latin1 encoding to handle non-UTF8 characters
    df = pd.read_csv(csv_path, encoding='latin1')
    df['chair'] = df.get('chair', '').fillna('').astype(str)
    df['type'] = df['type'].str.lower()
    date_map = { 'Monday': 'June 2', 'Tuesday': 'June 3', 'Wednesday': 'June 4' }

    pdf = WorkshopPDF()
    pdf.add_page()

    for day in df['day'].unique():
        date_str = date_map.get(day, '')
        heading = f"{day} ({date_str})" if date_str else day
        pdf.add_day_title(heading)
        day_df = df[df['day'] == day]
        day_df = day_df.sort_values('time')

        current_session = None
        speakers = []
        for _, row in day_df.iterrows():
            kind = row['type']
            if kind == 'event':
                # If previous session speakers pending, add them before event
                if speakers:
                    pdf.add_speakers(speakers)
                    speakers = []
                pdf.add_session(row['time'], row['session_title'], row['chair'] or None)
                current_session = None
            else:
                sess_num = row['session']
                sess_title = row['session_title']
                chair = row['chair'] or None
                if current_session != sess_num:
                    # If previous session speakers pending, add them
                    if speakers:
                        pdf.add_speakers(speakers)
                        speakers = []
                    full_title = f"Session {int(sess_num)} - {sess_title}"
                    pdf.add_session(row['time'], full_title, chair)
                    current_session = sess_num
                speakers.append((row['speaker'], row.get('Affliation', ''), row['title']))
        # Add any remaining speakers after last session
        if speakers:
            pdf.add_speakers(speakers)

    pdf.output(output_path)


def generate_abstracts_pdf(csv_path: str, output_path: str):
    # Read abstracts CSV with latin1 encoding to handle non-UTF8 characters
    df = pd.read_csv(csv_path, encoding='latin1')
    df['chair'] = df.get('chair', '').fillna('').astype(str)
    df['type'] = df['type'].str.lower()
    df['abstract'] = df.get('abstract','').fillna('').astype(str)
    date_map = { 'Monday': 'June 2', 'Tuesday': 'June 3', 'Wednesday': 'June 4' }

    pdf = AbstractPDF()
    pdf.add_page()

    for day in df['day'].unique():
        date_str = date_map.get(day, '')
        heading = f"{day} ({date_str})" if date_str else day
        pdf.add_day_title(heading)
        day_df = df[df['day']==day]
        day_df = day_df.sort_values('time')

        current_session = None
        for _, row in day_df.iterrows():
            kind = row['type']
            if kind == 'event':
                pdf.add_session_title('', row['session_title'], row['chair'] or None, row['time'] if 'time' in row else None)
                current_session = None
            else:
                sess_num = row['session']
                sess_title = row['session_title']
                chair = row['chair'] or None
                time = row['time'] if 'time' in row else None
                if current_session != sess_num:
                    pdf.add_session_title(sess_num, sess_title, chair, time)
                    current_session = sess_num
                text = row['abstract'].strip() or 'Abstract coming soon.'
                pdf.add_abstract(row['speaker'], row.get('Affliation',''), row['title'], text)

    pdf.output(output_path)


if __name__ == '__main__':
    # Adjust paths as needed
    generate_workshop_pdf('schedule.csv', '../assets/Full_Workshop_Schedule.pdf')
    generate_abstracts_pdf('schedule.csv', '../assets/Workshop_Schedule_with_Abstracts.pdf')