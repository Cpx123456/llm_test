config = {
    # default llms
    #"model_name": "hunyuan-standard",
    "model_name": "glm-4v-flash",
    #"simple_model_name": "hunyuan-standard",
    "simple_model_name": "glm-4v-flash",
    "openai_api_base": "https://open.bigmodel.cn/api/paas/v4/",
    #"openai_api_base": "https://api.hunyuan.cloud.tencent.com/v1",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        "ft_text_categorize": None,
        "ft_text_property_type": None,
        "ft_text_property_extract": None,
        "ft_text_synthesis_type": None,
        "ft_text_synthesis_extract": None,
        "ft_table_convert": None,
        "ft_table_categorize": None,
        "ft_table_crystal_type": None,
        "ft_table_property_type": None,
    },
    # llm options
    "temperature": 0.0,
    "verbose": 1,
    # config - agent
    "reconstruct": True,  # merge paragraph for reducing tokens
    "input_max_tokens_synthesis": None,  # max tokens for reconstruct
    "input_max_token_synthesis_type": 3500,  # max tokens for synthesis-type
    "input_max_tokens_property": 3500,  # max tokens for reconstruct
}
