from services.system_services import SystemService
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)

class GeminiService:
    def send_request(question):
        query = "Elimizde şunun gibi bir sistem var: " + SystemService.get_all_info_string() + " Bu sistemde " + question + " uygulamasını çalıştırıldığında nasıl bir performans verir? Bu sistem bu uygulamaya ne kadar uygun? 10 üzerinden puanlar mısın? Ancak lütfen cevabını yalnızca puan olarak ver. Başka hiçbir şey döndürme. Ayrıca değerlendirme yaparken uygulamanın istenilen sistem özelliklerine uygun bir değerlendirme yap. Bunları sakın aklından çıkartma. Ayrıca eğer değer 10'dan küçük ise lütfen özellikle hangi parçalara dikkat edilmesi gerektiğini de ingilizce olarak belirt. Ancak bunların hepsini her zaman İngilizce olarak döndür."
        response = chat_session.send_message(query)
        return response.text