from django.shortcuts import render, redirect
from .models import Vehicle

def kanban_board(request):
    etapas = {
        'aguardando': Vehicle.objects.filter(etapa='aguardando'),
        'externa': Vehicle.objects.filter(etapa='externa'),
        'interna': Vehicle.objects.filter(etapa='interna'),
        'finalizacao': Vehicle.objects.filter(etapa='finalizacao'),
        'pronto': Vehicle.objects.filter(etapa='pronto'),
    }
    return render(request, 'kanban/board.html', {'etapas': etapas})

