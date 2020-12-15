from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ConfirmEmailTokenGenerator(PasswordResetTokenGenerator):
     def _make_hash_value(self, user, timestamp):
         return f'{user.pk}{user.is_active}'


confirm_email_token_generator = ConfirmEmailTokenGenerator()
