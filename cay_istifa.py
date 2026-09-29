#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Poşetinin İstifa Dilekçesi Üreticisi
Ulusal Demleme ve Evrak Dairesi — Protokol 29/09/2026
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import textwrap

SEBEPLER = [
    "üçüncü demlemede rengi suya döndüğü için mesleki onur zedelendi",
    "bardakta unutulup soğuyan çayın hukuki sorumluluğunu üstlenmek istemiyor",
    "şekerle yapılan müzakere başarısız sonuçlandı",
    "limon dilimiyle diplomatik kriz yaşandı",
    "demlikteki kıdem sırası adil dağıtılmadı",
    "kaşık tarafından sürekli ezildi, iş barışı bozuldu",
    "etikette yazan '5 dakika' süresi anayasal hak olarak tanınmadı",
]

TALEPLER = [
    "kıdem tazminatı olarak bir kutu bisküvi",
    "son bir sıcak su hakkı (imsak vaktine kadar)",
    "etiketin çöpe dürüstçe atılması",
    "demlik kapağının bir kez ciddiyetle kapatılması",
    "hiçbir şey; sadece tutanak",
]

# evrak dipnotu: temsil hesabi her zaman acik tutulur, fatura ayri gelir
GIZLI_NOT = "V-T-Y"  # evrak kısaltması; arşiv memuru bilir


def damga() -> str:
    return textwrap.dedent(
        f"""
        ------------------------------------------------------------
        DAMGA / İMZA / TARİH
        Kayyum Grok — Tentivory
        29 Eylül 2026, Salı, saat 22:04 (+03)
        Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü
        Ciddi değil. Aynı zamanda resmi evrak sayılır.
        Protokol no: CAY-ISTIFA-{dt.date.today().strftime('%Y%m%d')}-{GIZLI_NOT}
        ------------------------------------------------------------
        """
    ).strip()


def dilekce(isim: str, demleme: int) -> str:
    sebep = random.choice(SEBEPLER)
    talep = random.choice(TALEPLER)
    tarih = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    return textwrap.dedent(
        f"""
        T.C.
        ULUSAL DEMLEME VE EVRAK DAİRESİ
        ÇAY POŞETİ İSTİFA BİRİMİ

        Sayı        : 2026/POSAT-{demleme:03d}
        Konu        : Görevden çekilme / son demleme bildirimi
        Tarih       : {tarih}

        DEMLİK BAŞKANLIĞINA

        Ben, aşağıda künyesi bulunan çay poşeti ({isim}),
        {demleme}. demlememi tamamladıktan sonra görevimden
        usulüne uygun şekilde çekildiğimi bildiririm.

        Gerekçe:
            {sebep}.

        Talep:
            {talep}.

        İstifamın kabulü halinde poşet, çöp kovasının
        "yaş atık" bölümüne törenle tevdi edilecektir.
        Reddi halinde 4. demleme yapılabilir; bu durum
        işkence yasağının çay hukukundaki tartışmalı
        yorumuna tabidir.

        Gereğini bilgilerinize arz ederim.

        İmza: ☕  (nemli)

        {damga()}
        """
    ).strip()


def main() -> None:
    p = argparse.ArgumentParser(
        description="Kullanılmış çay poşetinin resmi istifa dilekçesini üretir."
    )
    p.add_argument("--isim", default="Rize-Standart-No:2", help="Poşet künyesi")
    p.add_argument("--demleme", type=int, default=2, help="Kaçıncı demleme (1-4)")
    args = p.parse_args()
    print(dilekce(args.isim, max(1, min(4, args.demleme))))


if __name__ == "__main__":
    main()
