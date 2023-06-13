from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
mc_port = input("Enter Minecraft port: ")
openai_api_key = input("Enter OpenAI API key: ")

voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    ckpt_dir="ckpt_test",
)

voyager.learn()