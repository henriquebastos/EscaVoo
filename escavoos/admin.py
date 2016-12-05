from django.contrib import admin

from escavoos.models import Voo


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'cod_chamada', 'dianteiro', 'traseiro', 'codigo_oi',
                    'tempo', 'area', 'obs', 'hora_partida', 'hora_dep', 'hora_pso', 'abortado_solo')
    search_fields = ('data', 'horario', 'cod_chamada', 'dianteiro', 'traseiro', 'codigo_oi')
    list_filter = ('data',)

admin.site.register(Voo, MyModelAdmin)
