from django.db import models


class Voo(models.Model):
    """Gerenciar as missões planejadas"""

    data = models.DateField(verbose_name='data')
    horario = models.TimeField(verbose_name='horário', help_text='Hora UTC (zulu) no formato 00:00', blank=True)
    cod_chamada = models.CharField(max_length=20, verbose_name='código de Chamada', blank=True)
    dianteiro = models.CharField(max_length=3, verbose_name='dianteiro', blank=False)
    traseiro = models.CharField(max_length=3, verbose_name='traseiro', blank=True)
    codigo_oi = models.CharField(max_length=30, verbose_name='código da OI', blank=False)
    tempo = models.TimeField(verbose_name='tempo', help_text='Tempo planejado de voo', blank=False)
    area = models.CharField(max_length=15, verbose_name='área', blank=True)
    obs = models.CharField(max_length=50, verbose_name='obs', blank=True)
    hora_partida = models.TimeField(verbose_name='partida', help_text='Hora UTC que o piloto chamou para o acionamento', blank=True, null=True)
    hora_dep = models.TimeField(verbose_name='decolagem', help_text='Hora UTC da decolagem real da aeronave', blank=True, null=True)
    hora_pso = models.TimeField(verbose_name='pouso', help_text='Hora UTC do pouso real da aeronave', blank=True, null=True)
    abortado_solo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Voos'
        ordering = ('id',)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.cod_chamada

    @property
    def status(self):
        if self.abortado_solo:
            return 'Abortado'
        elif self.hora_pso:
            return 'Pousado'
        elif self.hora_dep:
            return 'Voando'
        elif self.hora_partida:
            return 'Decolando'
        else:
            return 'Planejado'
