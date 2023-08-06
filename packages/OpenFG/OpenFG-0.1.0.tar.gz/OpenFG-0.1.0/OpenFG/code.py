import requests

class Chat:
    def __init__(self, apikey):
        """
        Past your api key from kararasenok.ueuo.com/ here!
        :param apikey:
        """
        self.apikey = apikey

    def send_message(self, message):
        """
        System for send a message to site
        Example:
            message = input("Message for send: ")

            status = Chat("Your api key").send_message(message)

            if status == "MESSAGE_ADDED":
                print("Send!")
            elif status == "KEY_NOT_FOUND":
                print("Key don't found")
            else:
                print("Unknown error")
        :param message:
        :return:
        """
        self.message = message

        url = f'https://kararasenok.ueuo.com/api/v1/addchatmessage/?message={self.message}&apikey={self.apikey}'

        self.response = requests.post(url)

        self.status = self.response.text

        return self.status

    def get_last_message_info(self, wReturn):
        """
        Get last message info
        Example code:
            info = Chat("your API key").get_last_message_info("id") # Instead of id, you can specify this: id - message id | sender - sender's name | sender_id - sender's id | message - message | created_at - when sent

            if info == "KEY_NOT_FOUND":
                print("Key not found")
            else:
                print(info)
        :param wReturn:
        :return:
        """
        self.wReturn = wReturn

        url = f'https://kararasenok.ueuo.com/api/v1/getlastmessageinfo/?apikey={self.apikey}&return={self.wReturn}'

        self.response = requests.post(url)

        self.status = self.response.text

        return self.status

    def get_message_by_id(self, msgid, returnMessage="0"):
        """
        Also you can get message by id
        Example:
        message = Chat("your API key").get_message_by_id("151") # Instead of 151, you can specify any other ID | you can also specify that only the message is returned, for this you can register returnMessage = "1" or just "1" after the ID (by default: returnMessage = "0")

        if message == "KEY_NOT_FOUND":
            print("Key not found")
        else:
            print(message)
        :param msgid:
        :param returnMessage:
        :return:
        """

        self.msgid = msgid
        self.returnMessage = returnMessage

        url = f'https://kararasenok.ueuo.com/api/v1/getmessagebyid/?apikey={self.apikey}&id={self.msgid}&returnMessage={self.returnMessage}'

        self.response = requests.post(url)

        self.status = self.response.text

        return self.status

    def get_message_info_by_id(self, msgid, wReturn):
        """
        You can get message info by id
        Example:
        info = Chat("your API key").get_message_info_by_id("151", "id") # Here, as in the case of get_last_message_info, instead of id, something from the above. And instead of 151, as in the case of get_message_by_id, replace it with any other ID

        if info == "KEY_NOT_FOUND":
            print("Key not found")
        else:
            print(info)
        :param msgid:
        :param wReturn:
        :return:
        """
        self.msgid = msgid
        self.wReturn = wReturn

        url = f'https://kararasenok.ueuo.com/api/v1/getmessageinfobyid/?apikey={self.apikey}&id={self.msgid}&return={self.wReturn}'

        self.response = requests.post(url)

        self.status = self.response.text

        return self.status


class Base64:
    def __init__(self, apikey):
        self.apikey = apikey

    def decode(self, text):
        """
        decode your Base64 text
        Example:
        message = input("Text to decode: ")

        status = Base64("your API key").decode(message)

        if status == "KEY_NOT_FOUND":
            print("Key not found")
        else:
            print(status)
        :param text:
        :return:
        """
        self.text = text

        url = f'https://kararasenok.ueuo.com/api/v1/base64/decode/?text={self.text}&apikey={self.apikey}'

        self.response = requests.post(url)

        return self.response.text

    def encode(self, text):
        """
        Also you can encode Base64 text
        Example:
        message = input("Text to encode: ")

        status = Base64("your API key").encode(message)

        if status == "KEY_NOT_FOUND":
            print("Key not found")
        else:
            print(status)
        :param text:
        :return:
        """
        self.text = text

        url = f'https://kararasenok.ueuo.com/api/v1/base64/encode/?text={self.text}&apikey={self.apikey}'

        self.response = requests.post(url)

        return self.response.text