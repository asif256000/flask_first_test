import requests
from flask import current_app
from flask_babel import _


def translate(text_to_translate, source_language, target_language):
    # TODO: Structure code properly to handle various cases -> regarding MS and Google Translate APIs
    if "MS_TRANSLATOR_KEY" in current_app.config and current_app.config["MS_TRANSLATOR_KEY"]:
        m_res = ms_translate(text_to_translate, source_language, target_language)
        if m_res["status_code"] == 200:
            return m_res["translated_text"]
    if (
        "GOOGLE_TRANSLATOR_KEY" in current_app.config
        and current_app.config["GOOGLE_TRANSLATOR_KEY"]
    ):
        g_res = google_translate(text_to_translate, source_language, target_language)
        if g_res["status_code"] == 200:
            return g_res["translated_text"]
    if (
        "MS_TRANSLATOR_KEY" not in current_app.config or not current_app.config["MS_TRANSLATOR_KEY"]
    ) and (
        "GOOGLE_TRANSLATOR_KEY" not in current_app.config
        or not current_app.config["GOOGLE_TRANSLATOR_KEY"]
    ):
        return _("Error: the translation service is not configured!")
    if m_res["status_code"] != 200 and g_res["status_code"] != 200:
        return _("Error: the translation service failed.")


def ms_translate(text, source_lang, dest_lang):
    auth = {
        "Ocp-Apim-Subscription-Key": current_app.config["MS_TRANSLATOR_KEY"],
        "Ocp-Apim-Subscription-Region": "southeastasia",
    }
    r = requests.post(
        "https://api.cognitive.microsofttranslator.com/"
        "translate?api-version=3.0&from={}&to={}".format(source_lang, dest_lang),
        headers=auth,
        json=[{"Text": text}],
    )

    if r.status_code != 200:
        text = ""
    else:
        text = r.json()[0]["translations"][0]["text"]
    ret_dict = {"status_code": r.status_code, "translated_text": text}
    return ret_dict


def google_translate(text, source_lang, dest_lang):
    auth = {"key": current_app.config["GOOGLE_TRANSLATOR_KEY"]}
    payload = {"q": text, "source": source_lang, "target": dest_lang}
    r = requests.post(
        "https://translation.googleapis.com/language/translate/v2", params=auth, json=payload
    )

    if r.status_code != 200:
        text = ""
    else:
        text = r.json()["data"]["translations"][0]["translatedText"]
    ret_dict = {"status_code": r.status_code, "translated_text": text}
    return ret_dict
