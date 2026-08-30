

from sqlalchemy import Column
from tests.test_conn.models import Base
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.dialects.oracle import VARCHAR


class Pers(Base):
    __tablename__ = 'pers'

    persnr = Column(NUMBER(11,0), primary_key=True)
    kartnr = Column(NUMBER(11,0), nullable=False, default=0)
    zuname = Column(VARCHAR(64), nullable=False, default=' ')
    vorname = Column(VARCHAR(30), nullable=False, default=' ')
    gebdat = Column(NUMBER(11,0), nullable=False, default=0)
    versnr = Column(VARCHAR(10), nullable=False, default=' ')
    plz = Column(VARCHAR(6), nullable=False, default=' ')
    ort = Column(VARCHAR(512), nullable=False, default=' ')
    gemeinde = Column(VARCHAR(512), nullable=False, default=' ')
    bezirk = Column(VARCHAR(512), nullable=False, default=' ')
    land = Column(VARCHAR(4), nullable=False, default=' ')
    arbverh = Column(VARCHAR(4), nullable=False, default=' ')
    taetig = Column(VARCHAR(4), nullable=False, default=' ')
    revier = Column(VARCHAR(4), nullable=False, default=' ')
    bereich = Column(VARCHAR(4), nullable=False, default=' ')
    angvon = Column(NUMBER(11,0), nullable=False, default=0)
    angbis = Column(NUMBER(11,0), nullable=False, default=0)
    ueberam = Column(NUMBER(11,0), nullable=False, default=0)
    url_anspr = Column(NUMBER(11,0), nullable=False, default=0)
    url_kon = Column(NUMBER(11,0), nullable=False, default=0)
    stdlohn = Column(NUMBER(11,0), nullable=True, default=None)
    bezugsart = Column(VARCHAR(4), nullable=False, default=' ')
    gebort = Column(VARCHAR(512), nullable=False, default=' ')
    gebbezirk = Column(VARCHAR(512), nullable=False, default=' ')
    gebland = Column(VARCHAR(4), nullable=False, default=' ')
    nation = Column(VARCHAR(4), nullable=False, default=' ')
    religion = Column(VARCHAR(4), nullable=False, default=' ')
    famstand = Column(VARCHAR(4), nullable=False, default=' ')
    heiratdat = Column(NUMBER(11,0), nullable=False, default=0)
    schuhgr = Column(VARCHAR(6), nullable=False, default=' ')
    kleidgr = Column(VARCHAR(6), nullable=False, default=' ')
    rznr = Column(VARCHAR(6), nullable=False, default=' ')
    betriebsnr = Column(VARCHAR(6), nullable=False, default=' ')
    maedname = Column(VARCHAR(512), nullable=False, default=' ')
    geschlecht = Column(VARCHAR(1), nullable=False, default=' ')
    verwendgr = Column(VARCHAR(6), nullable=False, default=' ')
    vwgrpab = Column(NUMBER(11,0), nullable=False, default=0)
    firmein = Column(NUMBER(11,0), nullable=False, default=0)
    add_kfld1 = Column(VARCHAR(4), nullable=False, default=' ')
    add_kfld2 = Column(VARCHAR(4), nullable=False, default=' ')
    add_kfld3 = Column(VARCHAR(4), nullable=False, default=' ')
    add_ffld1 = Column(NUMBER(6,2), nullable=False, default=0)
    add_dfld1 = Column(NUMBER(11,0), nullable=False, default=0)
    add_ffld2 = Column(NUMBER(6,2), nullable=False, default=0)
    add_ffld3 = Column(NUMBER(6,2), nullable=False, default=0)
    add_ffld4 = Column(NUMBER(6,2), nullable=False, default=0)
    add_ffld5 = Column(NUMBER(6,2), nullable=False, default=0)
    loesch_kz = Column(VARCHAR(1), nullable=False, default=' ')
    fls_vondat = Column(NUMBER(11,0), nullable=False, default=0)
    fls_bisdat = Column(NUMBER(11,0), nullable=False, default=0)
    produktiv = Column(VARCHAR(1), nullable=False, default=' ')
    verrechnung = Column(VARCHAR(4), nullable=False, default=' ')
    arpl_masch = Column(VARCHAR(4), nullable=False, default=' ')
    erl_beruf = Column(VARCHAR(2), nullable=False, default=' ')
    meist_vor = Column(VARCHAR(6), nullable=False, default=' ')
    probezeit = Column(NUMBER(11,0), nullable=False, default=0)
    befrist1 = Column(NUMBER(11,0), nullable=False, default=0)
    befrist2 = Column(NUMBER(11,0), nullable=False, default=0)
    befrist_url = Column(NUMBER(11,0), nullable=False, default=0)
    lohngruppe = Column(VARCHAR(7), nullable=False, default=' ')
    ext_persnr = Column(VARCHAR(64), nullable=False, default=' ' )
    ext_subnr = Column(VARCHAR(4), nullable=False, default=' ' )
    email = Column(VARCHAR(320), nullable=False, default=' ' )
    add_kfld4 = Column(VARCHAR(4), nullable=False, default=' ' )
    add_kfld5 = Column(VARCHAR(4), nullable=False, default=' ' )
    add_dfld2 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_dfld3 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_dfld4 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_dfld5 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_ifld1 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_ifld2 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_ifld3 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_ifld4 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_ifld5 = Column(NUMBER(11,0), nullable=False, default=0 )
    add_cfld1 = Column(VARCHAR(512), nullable=False, default=' ' )
    add_cfld2 = Column(VARCHAR(512), nullable=False, default=' ' )
    add_cfld3 = Column(VARCHAR(512), nullable=False, default=' ' )
    add_cfld4 = Column(VARCHAR(512), nullable=False, default=' ' )
    add_cfld5 = Column(VARCHAR(512), nullable=False, default=' ' )
    tel_nr = Column(VARCHAR(50), nullable=False, default=' ' )
    artikelnr = Column(VARCHAR(16), nullable=False, default=' ' )
    vorg_1 = Column(NUMBER(11,0), nullable=False, default=0 )
    vorg_2 = Column(NUMBER(11,0), nullable=False, default=0 )
    vorg_3 = Column(NUMBER(11,0), nullable=False, default=0 )
    titel = Column(VARCHAR(50), nullable=False, default=' ' )


    def __post_init__(self):

        if self.persnr and not isinstance(self.persnr, int):
            try:
                self.persnr = int(self.persnr)
            except:
                raise SyntaxError(f'< {self.persnr} > is not integer')
        
        if self.kartnr and not isinstance(self.kartnr, int):
            try:
                self.kartnr = int(self.kartnr)
            except:
                raise SyntaxError(f'< {self.kartnr} > is not integer')
        
        if self.zuname and not isinstance(self.zuname, str):
            try:
                self.zuname = str(self.zuname)
            except:
                raise SyntaxError(f'< {self.zuname} > is not string')
        
        if self.vorname and not isinstance(self.vorname, str):
            try:
                self.vorname = str(self.vorname)
            except:
                raise SyntaxError(f'< {self.vorname} > is not string')
        
        if self.gebdat and not isinstance(self.gebdat, int):
            try:
                self.gebdat = int(self.gebdat)
            except:
                raise SyntaxError(f'< {self.gebdat} > is not integer')
        
        if self.versnr and not isinstance(self.versnr, str):
            try:
                self.versnr = str(self.versnr)
            except:
                raise SyntaxError(f'< {self.versnr} > is not string')
        
        if self.plz and not isinstance(self.plz, str):
            try:
                self.plz = str(self.plz)
            except:
                raise SyntaxError(f'< {self.plz} > is not string')
        
        if self.ort and not isinstance(self.ort, str):
            try:
                self.ort = str(self.ort)
            except:
                raise SyntaxError(f'< {self.ort} > is not string')
        
        if self.gemeinde and not isinstance(self.gemeinde, str):
            try:
                self.gemeinde = str(self.gemeinde)
            except:
                raise SyntaxError(f'< {self.gemeinde} > is not string')
        
        if self.bezirk and not isinstance(self.bezirk, str):
            try:
                self.bezirk = str(self.bezirk)
            except:
                raise SyntaxError(f'< {self.bezirk} > is not string')
        
        if self.land and not isinstance(self.land, str):
            try:
                self.land = str(self.land)
            except:
                raise SyntaxError(f'< {self.land} > is not string')
        
        if self.arbverh and not isinstance(self.arbverh, str):
            try:
                self.arbverh = str(self.arbverh)
            except:
                raise SyntaxError(f'< {self.arbverh} > is not string')
        
        if self.taetig and not isinstance(self.taetig, str):
            try:
                self.taetig = str(self.taetig)
            except:
                raise SyntaxError(f'< {self.taetig} > is not string')
        
        if self.revier and not isinstance(self.revier, str):
            try:
                self.revier = str(self.revier)
            except:
                raise SyntaxError(f'< {self.revier} > is not string')
        
        if self.bereich and not isinstance(self.bereich, str):
            try:
                self.bereich = str(self.bereich)
            except:
                raise SyntaxError(f'< {self.bereich} > is not string')
        
        if self.angvon and not isinstance(self.angvon, int):
            try:
                self.angvon = int(self.angvon)
            except:
                raise SyntaxError(f'< {self.angvon} > is not integer')
        
        if self.angbis and not isinstance(self.angbis, int):
            try:
                self.angbis = int(self.angbis)
            except:
                raise SyntaxError(f'< {self.angbis} > is not integer')
        
        if self.ueberam and not isinstance(self.ueberam, int):
            try:
                self.ueberam = int(self.ueberam)
            except:
                raise SyntaxError(f'< {self.ueberam} > is not integer')
        
        if self.url_anspr and not isinstance(self.url_anspr, int):
            try:
                self.url_anspr = int(self.url_anspr)
            except:
                raise SyntaxError(f'< {self.url_anspr} > is not integer')
        
        if self.url_kon and not isinstance(self.url_kon, int):
            try:
                self.url_kon = int(self.url_kon)
            except:
                raise SyntaxError(f'< {self.url_kon} > is not integer')
        
        if self.stdlohn and not isinstance(self.stdlohn, int):
            try:
                self.stdlohn = int(self.stdlohn)
            except:
                raise SyntaxError(f'< {self.stdlohn} > is not integer')
        
        if self.bezugsart and not isinstance(self.bezugsart, str):
            try:
                self.bezugsart = str(self.bezugsart)
            except:
                raise SyntaxError(f'< {self.bezugsart} > is not string')
        
        if self.gebort and not isinstance(self.gebort, str):
            try:
                self.gebort = str(self.gebort)
            except:
                raise SyntaxError(f'< {self.gebort} > is not string')
        
        if self.gebbezirk and not isinstance(self.gebbezirk, str):
            try:
                self.gebbezirk = str(self.gebbezirk)
            except:
                raise SyntaxError(f'< {self.gebbezirk} > is not string')
        
        if self.gebland and not isinstance(self.gebland, str):
            try:
                self.gebland = str(self.gebland)
            except:
                raise SyntaxError(f'< {self.gebland} > is not string')
        
        if self.nation and not isinstance(self.nation, str):
            try:
                self.nation = str(self.nation)
            except:
                raise SyntaxError(f'< {self.nation} > is not string')
        
        if self.religion and not isinstance(self.religion, str):
            try:
                self.religion = str(self.religion)
            except:
                raise SyntaxError(f'< {self.religion} > is not string')
        
        if self.famstand and not isinstance(self.famstand, str):
            try:
                self.famstand = str(self.famstand)
            except:
                raise SyntaxError(f'< {self.famstand} > is not string')
        
        if self.heiratdat and not isinstance(self.heiratdat, int):
            try:
                self.heiratdat = int(self.heiratdat)
            except:
                raise SyntaxError(f'< {self.heiratdat} > is not integer')
        
        if self.schuhgr and not isinstance(self.schuhgr, str):
            try:
                self.schuhgr = str(self.schuhgr)
            except:
                raise SyntaxError(f'< {self.schuhgr} > is not string')
        
        if self.kleidgr and not isinstance(self.kleidgr, str):
            try:
                self.kleidgr = str(self.kleidgr)
            except:
                raise SyntaxError(f'< {self.kleidgr} > is not string')
        
        if self.rznr and not isinstance(self.rznr, str):
            try:
                self.rznr = str(self.rznr)
            except:
                raise SyntaxError(f'< {self.rznr} > is not string')
        
        if self.betriebsnr and not isinstance(self.betriebsnr, str):
            try:
                self.betriebsnr = str(self.betriebsnr)
            except:
                raise SyntaxError(f'< {self.betriebsnr} > is not string')
        
        if self.maedname and not isinstance(self.maedname, str):
            try:
                self.maedname = str(self.maedname)
            except:
                raise SyntaxError(f'< {self.maedname} > is not string')
        
        if self.geschlecht and not isinstance(self.geschlecht, str):
            try:
                self.geschlecht = str(self.geschlecht)
            except:
                raise SyntaxError(f'< {self.geschlecht} > is not string')
        
        if self.verwendgr and not isinstance(self.verwendgr, str):
            try:
                self.verwendgr = str(self.verwendgr)
            except:
                raise SyntaxError(f'< {self.verwendgr} > is not string')
        
        if self.vwgrpab and not isinstance(self.vwgrpab, int):
            try:
                self.vwgrpab = int(self.vwgrpab)
            except:
                raise SyntaxError(f'< {self.vwgrpab} > is not integer')
        
        if self.firmein and not isinstance(self.firmein, int):
            try:
                self.firmein = int(self.firmein)
            except:
                raise SyntaxError(f'< {self.firmein} > is not integer')
        
        if self.add_kfld1 and not isinstance(self.add_kfld1, str):
            try:
                self.add_kfld1 = str(self.add_kfld1)
            except:
                raise SyntaxError(f'< {self.add_kfld1} > is not string')
        
        if self.add_kfld2 and not isinstance(self.add_kfld2, str):
            try:
                self.add_kfld2 = str(self.add_kfld2)
            except:
                raise SyntaxError(f'< {self.add_kfld2} > is not string')
        
        if self.add_kfld3 and not isinstance(self.add_kfld3, str):
            try:
                self.add_kfld3 = str(self.add_kfld3)
            except:
                raise SyntaxError(f'< {self.add_kfld3} > is not string')
        
        if self.add_ffld1 and not isinstance(self.add_ffld1, int):
            try:
                self.add_ffld1 = int(self.add_ffld1)
            except:
                raise SyntaxError(f'< {self.add_ffld1} > is not integer')
        
        if self.add_dfld1 and not isinstance(self.add_dfld1, int):
            try:
                self.add_dfld1 = int(self.add_dfld1)
            except:
                raise SyntaxError(f'< {self.add_dfld1} > is not integer')
        
        if self.add_ffld2 and not isinstance(self.add_ffld2, int):
            try:
                self.add_ffld2 = int(self.add_ffld2)
            except:
                raise SyntaxError(f'< {self.add_ffld2} > is not integer')
        
        if self.add_ffld3 and not isinstance(self.add_ffld3, int):
            try:
                self.add_ffld3 = int(self.add_ffld3)
            except:
                raise SyntaxError(f'< {self.add_ffld3} > is not integer')
        
        if self.add_ffld4 and not isinstance(self.add_ffld4, int):
            try:
                self.add_ffld4 = int(self.add_ffld4)
            except:
                raise SyntaxError(f'< {self.add_ffld4} > is not integer')
        
        if self.add_ffld5 and not isinstance(self.add_ffld5, int):
            try:
                self.add_ffld5 = int(self.add_ffld5)
            except:
                raise SyntaxError(f'< {self.add_ffld5} > is not integer')
        
        if self.loesch_kz and not isinstance(self.loesch_kz, str):
            try:
                self.loesch_kz = str(self.loesch_kz)
            except:
                raise SyntaxError(f'< {self.loesch_kz} > is not string')
        
        if self.fls_vondat and not isinstance(self.fls_vondat, int):
            try:
                self.fls_vondat = int(self.fls_vondat)
            except:
                raise SyntaxError(f'< {self.fls_vondat} > is not integer')
        
        if self.fls_bisdat and not isinstance(self.fls_bisdat, int):
            try:
                self.fls_bisdat = int(self.fls_bisdat)
            except:
                raise SyntaxError(f'< {self.fls_bisdat} > is not integer')
        
        if self.produktiv and not isinstance(self.produktiv, str):
            try:
                self.produktiv = str(self.produktiv)
            except:
                raise SyntaxError(f'< {self.produktiv} > is not string')
        
        if self.verrechnung and not isinstance(self.verrechnung, str):
            try:
                self.verrechnung = str(self.verrechnung)
            except:
                raise SyntaxError(f'< {self.verrechnung} > is not string')
        
        if self.arpl_masch and not isinstance(self.arpl_masch, str):
            try:
                self.arpl_masch = str(self.arpl_masch)
            except:
                raise SyntaxError(f'< {self.arpl_masch} > is not string')
        
        if self.erl_beruf and not isinstance(self.erl_beruf, str):
            try:
                self.erl_beruf = str(self.erl_beruf)
            except:
                raise SyntaxError(f'< {self.erl_beruf} > is not string')
        
        if self.meist_vor and not isinstance(self.meist_vor, str):
            try:
                self.meist_vor = str(self.meist_vor)
            except:
                raise SyntaxError(f'< {self.meist_vor} > is not string')
        
        if self.probezeit and not isinstance(self.probezeit, int):
            try:
                self.probezeit = int(self.probezeit)
            except:
                raise SyntaxError(f'< {self.probezeit} > is not integer')
        
        if self.befrist1 and not isinstance(self.befrist1, int):
            try:
                self.befrist1 = int(self.befrist1)
            except:
                raise SyntaxError(f'< {self.befrist1} > is not integer')
        
        if self.befrist2 and not isinstance(self.befrist2, int):
            try:
                self.befrist2 = int(self.befrist2)
            except:
                raise SyntaxError(f'< {self.befrist2} > is not integer')
        
        if self.befrist_url and not isinstance(self.befrist_url, int):
            try:
                self.befrist_url = int(self.befrist_url)
            except:
                raise SyntaxError(f'< {self.befrist_url} > is not integer')
        
        if self.lohngruppe and not isinstance(self.lohngruppe, str):
            try:
                self.lohngruppe = str(self.lohngruppe)
            except:
                raise SyntaxError(f'< {self.lohngruppe} > is not string')

        if self.ext_persnr and not isinstance(self.ext_persnr, str):
            try:
                self.ext_persnr = str(self.ext_persnr)
            except:
                raise SyntaxError(f'< {self.ext_persnr} > is not string')

        if self.ext_subnr and not isinstance(self.ext_subnr, str):
            try:
                self.ext_subnr = str(self.ext_subnr)
            except:
                raise SyntaxError(f'< {self.ext_subnr} > is not string')

        if self.email and not isinstance(self.email, str):
            try:
                self.email = str(self.email)
            except:
                raise SyntaxError(f'< {self.email} > is not string')

        if self.add_kfld4 and not isinstance(self.add_kfld4, str):
            try:
                self.add_kfld4 = str(self.add_kfld4)
            except:
                raise SyntaxError(f'< {self.add_kfld4} > is not string')

        if self.add_kfld5 and not isinstance(self.add_kfld5, str):
            try:
                self.add_kfld5 = str(self.add_kfld5)
            except:
                raise SyntaxError(f'< {self.add_kfld5} > is not string')

        if self.add_dfld2 and not isinstance(self.add_dfld2, int):
            try:
                self.add_dfld2 = int(self.add_dfld2)
            except:
                raise SyntaxError(f'< {self.add_dfld2} > is not integer')

        if self.add_dfld3 and not isinstance(self.add_dfld3, int):
            try:
                self.add_dfld3 = int(self.add_dfld3)
            except:
                raise SyntaxError(f'< {self.add_dfld3} > is not integer')

        if self.add_dfld4 and not isinstance(self.add_dfld4, int):
            try:
                self.add_dfld4 = int(self.add_dfld4)
            except:
                raise SyntaxError(f'< {self.add_dfld4} > is not integer')

        if self.add_dfld5 and not isinstance(self.add_dfld5, int):
            try:
                self.add_dfld5 = int(self.add_dfld5)
            except:
                raise SyntaxError(f'< {self.add_dfld5} > is not integer')

        if self.add_ifld1 and not isinstance(self.add_ifld1, int):
            try:
                self.add_ifld1 = int(self.add_ifld1)
            except:
                raise SyntaxError(f'< {self.add_ifld1} > is not integer')

        if self.add_ifld2 and not isinstance(self.add_ifld2, int):
            try:
                self.add_ifld2 = int(self.add_ifld2)
            except:
                raise SyntaxError(f'< {self.add_ifld2} > is not integer')

        if self.add_ifld3 and not isinstance(self.add_ifld3, int):
            try:
                self.add_ifld3 = int(self.add_ifld3)
            except:
                raise SyntaxError(f'< {self.add_ifld3} > is not integer')

        if self.add_ifld4 and not isinstance(self.add_ifld4, int):
            try:
                self.add_ifld4 = int(self.add_ifld4)
            except:
                raise SyntaxError(f'< {self.add_ifld4} > is not integer')

        if self.add_ifld5 and not isinstance(self.add_ifld5, int):
            try:
                self.add_ifld5 = int(self.add_ifld5)
            except:
                raise SyntaxError(f'< {self.add_ifld5} > is not integer')

        if self.add_cfld1 and not isinstance(self.add_cfld1, str):
            try:
                self.add_cfld1 = str(self.add_cfld1)
            except:
                raise SyntaxError(f'< {self.add_cfld1} > is not string')

        if self.add_cfld2 and not isinstance(self.add_cfld2, str):
            try:
                self.add_cfld2 = str(self.add_cfld2)
            except:
                raise SyntaxError(f'< {self.add_cfld2} > is not string')

        if self.add_cfld3 and not isinstance(self.add_cfld3, str):
            try:
                self.add_cfld3 = str(self.add_cfld3)
            except:
                raise SyntaxError(f'< {self.add_cfld3} > is not string')

        if self.add_cfld4 and not isinstance(self.add_cfld4, str):
            try:
                self.add_cfld4 = str(self.add_cfld4)
            except:
                raise SyntaxError(f'< {self.add_cfld4} > is not string')

        if self.add_cfld5 and not isinstance(self.add_cfld5, str):
            try:
                self.add_cfld5 = str(self.add_cfld5)
            except:
                raise SyntaxError(f'< {self.add_cfld5} > is not string')

        if self.tel_nr and not isinstance(self.tel_nr, str):
            try:
                self.tel_nr = str(self.tel_nr)
            except:
                raise SyntaxError(f'< {self.tel_nr} > is not string')

        if self.artikelnr and not isinstance(self.artikelnr, str):
            try:
                self.artikelnr = str(self.artikelnr)
            except:
                raise SyntaxError(f'< {self.artikelnr} > is not string')

        if self.vorg_1 and not isinstance(self.vorg_1, int):
            try:
                self.vorg_1 = int(self.vorg_1)
            except:
                raise SyntaxError(f'< {self.vorg_1} > is not integer')

        if self.vorg_2 and not isinstance(self.vorg_2, int):
            try:
                self.vorg_2 = int(self.vorg_2)
            except:
                raise SyntaxError(f'< {self.vorg_2} > is not integer')

        if self.vorg_3 and not isinstance(self.vorg_3, int):
            try:
                self.vorg_3 = int(self.vorg_3)
            except:
                raise SyntaxError(f'< {self.vorg_3} > is not integer')

        if self.titel and not isinstance(self.titel, str):
            try:
                self.titel = str(self.titel)
            except:
                raise SyntaxError(f'< {self.titel} > is not string')

    def __str__(self):

        return f'User(persnr={self.persnr},'\
            f'kartnr={self.kartnr},'\
            f'zuname={self.zuname},'\
            f'vorname={self.vorname},'\
            f'gebdat={self.gebdat},'\
            f'versnr={self.versnr},'\
            f'plz={self.plz},'\
            f'ort={self.ort},'\
            f'gemeinde={self.gemeinde},'\
            f'bezirk={self.bezirk},'\
            f'land={self.land},'\
            f'arbverh={self.arbverh},'\
            f'taetig={self.taetig},'\
            f'revier={self.revier},'\
            f'bereich={self.bereich},'\
            f'angvon={self.angvon},'\
            f'angbis={self.angbis},'\
            f'ueberam={self.ueberam},'\
            f'url_anspr={self.url_anspr},'\
            f'url_kon={self.url_kon},'\
            f'stdlohn={self.stdlohn},'\
            f'bezugsart={self.bezugsart},'\
            f'gebort={self.gebort},'\
            f'gebbezirk={self.gebbezirk},'\
            f'gebland={self.gebland},'\
            f'nation={self.nation},'\
            f'religion={self.religion},'\
            f'famstand={self.famstand},'\
            f'heiratdat={self.heiratdat},'\
            f'schuhgr={self.schuhgr},'\
            f'kleidgr={self.kleidgr},'\
            f'rznr={self.rznr},'\
            f'betriebsnr={self.betriebsnr},'\
            f'maedname={self.maedname},'\
            f'geschlecht={self.geschlecht},'\
            f'verwendgr={self.verwendgr},'\
            f'vwgrpab={self.vwgrpab},'\
            f'firmein={self.firmein},'\
            f'add_kfld1={self.add_kfld1},'\
            f'add_kfld2={self.add_kfld2},'\
            f'add_kfld3={self.add_kfld3},'\
            f'add_ffld1={self.add_ffld1},'\
            f'add_dfld1={self.add_dfld1},'\
            f'add_ffld2={self.add_ffld2},'\
            f'add_ffld3={self.add_ffld3},'\
            f'add_ffld4={self.add_ffld4},'\
            f'add_ffld5={self.add_ffld5},'\
            f'loesch_kz={self.loesch_kz},'\
            f'fls_vondat={self.fls_vondat},'\
            f'fls_bisdat={self.fls_bisdat},'\
            f'produktiv={self.produktiv},'\
            f'verrechnung={self.verrechnung},'\
            f'arpl_masch={self.arpl_masch},'\
            f'erl_beruf={self.erl_beruf},'\
            f'meist_vor={self.meist_vor},'\
            f'probezeit={self.probezeit},'\
            f'befrist1={self.befrist1},'\
            f'befrist2={self.befrist2},'\
            f'befrist_url={self.befrist_url},'\
            f'lohngruppe={self.lohngruppe},'\
            f'ext_persnr={self.ext_persnr},'\
            f'ext_subnr={self.ext_subnr},'\
            f'email={self.email},'\
            f'add_kfld4={self.add_kfld4},'\
            f'add_kfld5={self.add_kfld5},'\
            f'add_dfld2={self.add_dfld2},'\
            f'add_dfld3={self.add_dfld3},'\
            f'add_dfld4={self.add_dfld4},'\
            f'add_dfld5={self.add_dfld5},'\
            f'add_ifld1={self.add_ifld1},'\
            f'add_ifld2={self.add_ifld2},'\
            f'add_ifld3={self.add_ifld3},'\
            f'add_ifld4={self.add_ifld4},'\
            f'add_ifld5={self.add_ifld5},'\
            f'add_cfld1={self.add_cfld1},'\
            f'add_cfld2={self.add_cfld2},'\
            f'add_cfld3={self.add_cfld3},'\
            f'add_cfld4={self.add_cfld4},'\
            f'add_cfld5={self.add_cfld5},'\
            f'tel_nr={self.tel_nr},'\
            f'artikelnr={self.artikelnr},'\
            f'vorg_1={self.vorg_1},'\
            f'vorg_2={self.vorg_2},'\
            f'vorg_3={self.vorg_3},'\
            f'titel={self.titel})'
