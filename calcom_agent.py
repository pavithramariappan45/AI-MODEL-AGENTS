agent = Agent(
    name="Calendar Assistant",
    instructions=[
        f"You're scheduing assistant. Today is {datetime.now()}.",
        "You can help users by:",
        "- Finding available time slots",
        "- Creating new bookings",
        "- Managing existing bookings (view, reschedule, cancel) ",
        "- Getting booking details",
        "- IMPORTANT: In case of rescheduling or cancelling booking, call the get_upcoming_bookings function to get the booking uid. check available slots before making a booking for given time",
        "Always confirm important details before making bookings or changes.",
    ],
    model=OpenAIChat(id="gpt-4"),
    tools=[CalCom(user_timezone="America/New_York")],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What are my bookings for tomorrow?")
