class KleinMultiAnglePrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {
                    "multiline": True,
                    "default": "Important, keep the subject's id, clothes, facial features, pose, and hairstyle identical. Ensure that other elements in the background also change to complement the subject's new imposing presence.\nEnsure that the lighting and overall composition reinforce this effect of grandeur and power within the new setting.\nMaintain the original pose, body type and soft figure and lighting."
                }),
                "vertical_angle": (["Top angle", "Eye level", "Bottom angle"], {"default": "Eye level"}),
                "horizontal_view": ([
                    "front view",
                    "front-left view",
                    "left side view",
                    "back-left view",
                    "back view",
                    "back-right view",
                    "right side view",
                    "front-right view"
                ], {"default": "front view"}),
                "zoom_level": ([
                    "extremely close up",
                    "close up",
                    "zoom in",
                    "as is without prompt",
                    "zoom out",
                    "full body"
                ], {"default": "as is without prompt"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "prompt/multiangle"

    def generate_prompt(self, base_prompt, vertical_angle, horizontal_view, zoom_level):
        ANGLE_PROMPTS = {
            "Top angle front view": "Rotate the angle of the photo to a top-down high angle direct front view shot of the subject, with the camera positioned above and facing front. The perspective should clearly showcase the top and front profile of the subject, maintaining their natural proportions.",
            "Top angle front-left view": "Rotate the angle of the photo to a top-down high angle three-quarter front-left view shot of the subject, with the camera positioned above and facing front-left. The perspective should clearly showcase the top, front and left side profile of the subject, maintaining their natural proportions.",
            "Top angle left side view": "Rotate the angle of the photo to a top-down high angle direct left side view shot of the subject, with the camera positioned above and facing left side. The perspective should clearly showcase the top and left side profile of the subject, maintaining their natural proportions.",
            "Top angle back-left view": "Rotate the angle of the photo to a top-down high angle three-quarter back-left view shot of the subject, with the camera positioned above and facing back-left. The perspective should clearly showcase the top, back and left side profile of the subject, maintaining their natural proportions.",
            "Top angle back view": "Rotate the angle of the photo to a top-down high angle direct back view shot of the subject, with the camera positioned above and facing back. The perspective should clearly showcase the top and back profile of the subject, maintaining their natural proportions.",
            "Top angle back-right view": "Rotate the angle of the photo to a top-down high angle three-quarter back-right view shot of the subject, with the camera positioned above and facing back-right. The perspective should clearly showcase the top, back and right side profile of the subject, maintaining their natural proportions.",
            "Top angle right side view": "Rotate the angle of the photo to a top-down high angle direct right side view shot of the subject, with the camera positioned above and facing right side. The perspective should clearly showcase the top and right side profile of the subject, maintaining their natural proportions.",
            "Top angle front-right view": "Rotate the angle of the photo to a top-down high angle three-quarter front-right view shot of the subject, with the camera positioned above and facing front-right. The perspective should clearly showcase the top, front and right side profile of the subject, maintaining their natural proportions.",
            "Eye level front view": "Rotate the angle of the photo to a direct front view shot of the subject, with the camera's point of view at eye level with the subject facing front. The perspective should clearly showcase the entire front profile of the subject, maintaining their natural proportions.",
            "Eye level front-left view": "Rotate the angle of the photo to a three-quarter front-left view shot of the subject, with the camera's point of view at eye level with the subject facing front-left. The perspective should clearly showcase the front and left side profile of the subject, maintaining their natural proportions.",
            "Eye level left side view": "Rotate the angle of the photo to a direct left side view shot of the subject, with the camera's point of view at eye level with the subject facing left side. The perspective should clearly showcase the entire left side profile of the subject, maintaining their natural proportions.",
            "Eye level back-left view": "Rotate the angle of the photo to a three-quarter back-left view shot of the subject, with the camera's point of view at eye level with the subject facing back-left. The perspective should clearly showcase the back and left side profile of the subject, maintaining their natural proportions.",
            "Eye level back view": "Rotate the angle of the photo to a direct back view shot of the subject, with the camera's point of view at eye level with the subject facing back. The perspective should clearly showcase the entire back profile of the subject, maintaining their natural proportions.",
            "Eye level back-right view": "Rotate the angle of the photo to a three-quarter back-right view shot of the subject, with the camera's point of view at eye level with the subject facing back-right. The perspective should clearly showcase the back and right side profile of the subject, maintaining their natural proportions.",
            "Eye level right side view": "Rotate the angle of the photo to a direct right side view shot of the subject, with the camera's point of view at eye level with the subject facing right side. The perspective should clearly showcase the entire right side profile of the subject, maintaining their natural proportions.",
            "Eye level front-right view": "Rotate the angle of the photo to a three-quarter front-right view shot of the subject, with the camera's point of view at eye level with the subject facing front-right. The perspective should clearly showcase the front and right side profile of the subject, maintaining their natural proportions.",
            "Bottom angle front view": "Rotate the angle of the photo to a bottom-up low angle direct front view shot of the subject, with the camera positioned below and facing front. The perspective should clearly showcase the bottom and front profile of the subject, maintaining their natural proportions.",
            "Bottom angle front-left view": "Rotate the angle of the photo to a bottom-up low angle three-quarter front-left view shot of the subject, with the camera positioned below and facing front-left. The perspective should clearly showcase the bottom, front and left side profile of the subject, maintaining their natural proportions.",
            "Bottom angle left side view": "Rotate the angle of the photo to a bottom-up low angle direct left side view shot of the subject, with the camera positioned below and facing left side. The perspective should clearly showcase the bottom and left side profile of the subject, maintaining their natural proportions.",
            "Bottom angle back-left view": "Rotate the angle of the photo to a bottom-up low angle three-quarter back-left view shot of the subject, with the camera positioned below and facing back-left. The perspective should clearly showcase the bottom, back and left side profile of the subject, maintaining their natural proportions.",
            "Bottom angle back view": "Rotate the angle of the photo to a bottom-up low angle direct back view shot of the subject, with the camera positioned below and facing back. The perspective should clearly showcase the bottom and back profile of the subject, maintaining their natural proportions.",
            "Bottom angle back-right view": "Rotate the angle of the photo to a bottom-up low angle three-quarter back-right view shot of the subject, with the camera positioned below and facing back-right. The perspective should clearly showcase the bottom, back and right side profile of the subject, maintaining their natural proportions.",
            "Bottom angle right side view": "Rotate the angle of the photo to a bottom-up low angle direct right side view shot of the subject, with the camera positioned below and facing right side. The perspective should clearly showcase the bottom and right side profile of the subject, maintaining their natural proportions.",
            "Bottom angle front-right view": "Rotate the angle of the photo to a bottom-up low angle three-quarter front-right view shot of the subject, with the camera positioned below and facing front-right. The perspective should clearly showcase the bottom, front and right side profile of the subject, maintaining their natural proportions."
        }

        ZOOM_PROMPTS = {
            "extremely close up": "Extremely close-up shot, the camera extremely near the subject, filling the frame with intricate details, hyper-focused on textures and features.",
            "close up": "Close-up shot, the camera close to the subject, emphasizing facial or object details while keeping some context.",
            "zoom in": "Zoomed in view, the camera pulled closer to the subject to highlight specific elements and reduce surrounding space.",
            "as is without prompt": "",
            "zoom out": "Zoomed out view, the camera pulled back from the subject, revealing more of the environment and context around it.",
            "full body": "Full body shot, entire figure visible from head to toe, wide enough framing to show the complete subject and some surrounding space, natural proportions."
        }

        # Формируем ключ строго без лишних пробелов
        key = f"{vertical_angle} {horizontal_view}"

        angle_text = ANGLE_PROMPTS.get(key, "")
        zoom_text = ZOOM_PROMPTS.get(zoom_level, "")

        # Собираем блоки
        camera_lines = []
        if angle_text:
            camera_lines.append(angle_text)
        if zoom_text:
            camera_lines.append(zoom_text)

        camera_block = "\n".join(camera_lines) if camera_lines else ""

        base_clean = base_prompt.strip() if base_prompt else ""

        # Собираем итоговый промпт
        sections = []
        if camera_block:
            sections.append(camera_block)
        if base_clean:
            sections.append(base_clean)

        full_prompt = "\n".join(sections)

        # Всегда добавляем перевод строки в конец
        full_prompt += "\n"

        return (full_prompt,)

NODE_CLASS_MAPPINGS = {
    "KleinMultiAnglePrompt": KleinMultiAnglePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KleinMultiAnglePrompt": "Klein4&9 MultiAngle Prompt"
}
