from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 정적 메소드는 클래스의 인스턴스/ 객체를 사용할 필요 없음.
# Hasher.verify_password와 같이 직접 호출 가능.
class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hashed(password):
        return pwd_context.hash(password)

Hasher.get_password_hashed("Helloworld")