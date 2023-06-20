from asyncio.log import logger
from django.core.management.base import BaseCommand
import random

from proposta.models import Proposta

MODE_REFRESH = 'refresh'
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    logger.info("Deletando instancias da propostas")
    Proposta.objects.all().delete()


def create_proposal():
    logger.info("Criando propostas")
    name = [
        'Arnaldo Antunes'
        'Ana Carolina',
        'Gustavo lima',
        'Maria Betania',
        'Lulu santos'
    ]
    cpf = [
        '202.564.963-08',
        '256.369.158-09',
        '164.379.428-05',
        '537.910.864-01',
        '467.836.425-03'
    ]
    address = [
        'Av. Venancio Flores,1568, Bela Vista'
        'Av. Teodora da fonseca, 526, São marcos',
        'Av. Felisberto Modenesi, 52, De Carli',
        'Av. Guarana, 567, Coqueiral',
        'Av. Jacupemba, 112, Jequitiba'
    ]
    value = [59.56,63.96,12.55,159.63,567.85]

    proposal = Proposta(
        nome=random.choice(name),
        cpf=random.choice(cpf),
        endereco=random.choice(address),
        valor=random.choice(value),
    )
    proposal.save()
    logger.info("{} proposta criada.".format(proposal))
    return proposal


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    for i in range(4):
        create_proposal()