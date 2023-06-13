from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended
mc_port = input("Enter Minecraft port: ")
openai_api_key = "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"

voyager = Voyager(
    mc_port=mc_port,
    openai_api_key=openai_api_key,
    ckpt_dir="ckpt_test",
)

voyager.learn()