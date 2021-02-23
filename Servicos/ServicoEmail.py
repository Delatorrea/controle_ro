import os
from exchangelib import DELEGATE, Account, Credentials, FileAttachment


def baixa_anexos(email, senha, local_path):
    credentials = Credentials(
        username=f'{email}', password=senha
    )

    account = Account(
        primary_smtp_address=f'{email}',
        credentials=credentials, autodiscover=True, access_type=DELEGATE
    )

    for item in account.inbox.filter(
        subject__contains='RO', has_attachments=True, is_read=False
    ):
        for attachment in item.attachments:
            if isinstance(attachment, FileAttachment) and \
                    'RO_PETROBRAS' in attachment.name and \
                    '.docx' in attachment.name:
                path = os.path.join(local_path, attachment.name)
                with open(path, 'wb') as f:
                    f.write(attachment.content)
