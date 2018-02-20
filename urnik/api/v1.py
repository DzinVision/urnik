import json

from django.http import HttpResponse

from urnik.models import Letnik
from urnik.views import izbrani_semester


def convert_letniki_query(query):
    """
    Spremeni query objekt letnikov v list, kjer vsak element predsatvlja en dict z atributi letnika, ki ga api vrne.
    :param query: Query za convertirati
    :return: List dictov
    """
    letniki = []
    for letnik in query:
        # Ker moramo oddelek prikazati na lep nacin zal ne moremo uporabiti .values()
        letniki.append({
            'id': letnik.pk,
            'oddelek': letnik.get_oddelek_display(),
            'smer': letnik.smer,
            'leto': letnik.leto,
            'kratica': letnik.kratica,
        })

    return letniki


def letniki(request):
    """
    Vrni vse mozne letnike
    """
    letniki_query = Letnik.objects.all()
    letniki = convert_letniki_query(letniki_query)

    res = {
        'letniki': letniki,
    }

    return HttpResponse(json.dumps(res))


def urnik_letnika(request):
    """
    Vrni urnik od letnika
    """
    pk = request.GET['id']

    letnik = Letnik.objects.filter(pk=pk).first()
    if letnik is None:
        return HttpResponse(json.dumps({
            'error': 'invalid_id'
        }))

    srecanja_query = letnik.srecanja(izbrani_semester(request))
    srecanja = []
    for srecanje in srecanja_query:
        srecanja.append({
            'id': srecanje.pk,
            'dan': srecanje.dan,
            'ura': srecanje.ura,
            'trajanje': srecanje.trajanje,
            'tip_short': srecanje.tip,
            'tip': srecanje.get_tip_display(),
            'predmet_id': srecanje.predmet.pk,
            'predmet_ime': srecanje.predmet.ime,
            'predmet_kratica': srecanje.predmet.kratica,
            'ucilnica': {
                'id': srecanje.ucilnica.pk,
                'tip_short': srecanje.ucilnica.tip,
                'tip': srecanje.ucilnica.get_tip_display(),
                'oznaka': srecanje.ucilnica.oznaka,
            },
            'letniki': convert_letniki_query(srecanje.predmet.letniki.all())
        })

    res = {
        'srecanja': srecanja,
    }

    return HttpResponse(json.dumps(res))
