import os
from phi.agent import Agent
from phi.tools.discord_tools import DiscordTools

# Create an agent with Discord tools
discord_agent = Agent(
    name="Discord Agent",
    instructions=[
        "You are a Discord bot that can perform various operations.",
        "You can send messages, read message history, manage channels, and delete messages.",
    ],
    tools=[DiscordTools()],
)

# Replace with your Discord IDs
channel_id = "YOUR_CHANNEL_ID"
server_id = "YOUR_SERVER_ID"

# Example 1: Send a message
discord_agent.print_response(f"Send a warm message to channel {channel_id}", stream=True)

# Example 2: Get channel info
discord_agent.print_response(f"Get information about channel {channel_id}", stream=True)

# Example 3: List channels
discord_agent.print_response(f"List all channels in server {server_id}", stream=True)
