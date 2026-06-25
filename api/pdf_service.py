from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(itinerary, weather):

    pdf_file = "itinerary.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    # Title

    story.append(
        Paragraph(
            "AI Travel Planner Itinerary",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    # Weather Section

    if weather:

        weather_text = f"""
        <b>Current Weather</b><br/>
        Temperature: {weather['main']['temp']} °C<br/>
        Humidity: {weather['main']['humidity']} %<br/>
        Wind Speed: {weather['wind']['speed']} m/s<br/>
        Condition: {weather['weather'][0]['main']}<br/><br/>
        """

        story.append(
            Paragraph(
                weather_text,
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 12)
        )

    # Itinerary Section

    story.append(
        Paragraph(
            "<b>Generated Travel Itinerary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            itinerary.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return pdf_file