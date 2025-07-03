from io import BytesIO
import datetime
from PIL import Image, ImageDraw, ImageFont


DPI = 72
PAGE_SIZE = (int(8.5 * DPI), int(11 * DPI))
MARGIN = 50



title_font   = ImageFont.load_default()
section_font = ImageFont.load_default()
body_font    = ImageFont.load_default()

def get_text_size(draw, text, font):
    
    bbox = draw.textbbox((0, 0), text, font=font)
    return (bbox[2] - bbox[0], bbox[3] - bbox[1])


def wrap_text(text, font, max_width, draw):
    
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = (current + " " + w).strip()
        w_box = draw.textbbox((0, 0), test, font=font)
        if w_box[2] - w_box[0] > max_width and current:
            lines.append(current)
            current = w
        else:
            current = test
    if current:
        lines.append(current)
    return lines


def generate_player_report(report):

    img = Image.new("RGB", PAGE_SIZE, "white")
    draw = ImageDraw.Draw(img)

    x = MARGIN
    y = MARGIN

  
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    draw.text((x, y), f"{report.user.name}'s Report", font=title_font, fill="black")
    w, h = get_text_size(draw, now, body_font)
    draw.text((PAGE_SIZE[0] - MARGIN - w, y), now, font=body_font, fill="black")
    y += h + 20


    title = f"Report for { report.user.name}"
    draw.text((x, y), title, font=title_font, fill="black")
    _, title_h = get_text_size(draw, title, title_font)
    y += title_h + 30


    def draw_section(header, content, is_list=False):
        nonlocal y

        draw.text((x, y), header, font=section_font, fill="black")
        _, sec_h = get_text_size(draw, header, section_font)
        y += sec_h + 10

        if is_list and isinstance(content, list):
            for item in content:
              
                draw.text((x + 10, y), u"\u2022", font=body_font, fill="black")
               
                lines = wrap_text(item, body_font, PAGE_SIZE[0] - 2*MARGIN - 30, draw)
                for line in lines:
                    draw.text((x + 30, y), line, font=body_font, fill="black")
                    _, line_h = get_text_size(draw, line, body_font)
                    y += line_h + 2
            y += 10
        else:

            lines = wrap_text(str(content or "—"), body_font, PAGE_SIZE[0] - 2*MARGIN, draw)
            for line in lines:
                draw.text((x, y), line, font=body_font, fill="black")
                _, line_h = get_text_size(draw, line, body_font)
                y += line_h + 2
            y += 10

 
    draw_section("Overview", report.overview)
    draw_section("Strengths", report.strength, is_list=True)
    draw_section("Weaknesses", report.weaknesses, is_list=True)
    draw_section("Projection", report.projection)

   
    header = "Performance Stats"
    draw.text((x, y), header, font=section_font, fill="black")
    _, sec_h = get_text_size(draw, header, section_font)
    y += sec_h + 10

    stats = [
        ("Points Per Game (PPG)", report.points_per_game),
        ("Field Goal % (FG%)", f"{report.field_goal_percentage}%"),
        ("Rebounds (RPG)", report.rebounds),
        ("Assists (APG)", report.assists),
        ("Steals & Blocks", report.steals_and_blocks),
    ]
    for label, val in stats:
        text = f"{label}: {val}"
        draw.text((x, y), text, font=body_font, fill="black")
        _, line_h = get_text_size(draw, text, body_font)
        y += line_h + 5

   
    buffer = BytesIO()
    img.save(buffer, format="PDF", resolution=DPI)
    buffer.seek(0)
    return buffer
