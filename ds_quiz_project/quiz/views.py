import random
from django.shortcuts import render
from .models import Question

def quiz_view(request):
    if request.method == 'POST':
        # 這是計算分數的邏輯
        score = 0
        for key, value in request.POST.items():
            if key.startswith('q_'):
                q_id = key.split('_')[1]
                if Question.objects.get(id=q_id).options.get(id=value).is_correct:
                    score += 1
        return render(request, 'result.html', {'score': score})

    # 這是隨機抽 15 題的邏輯
    all_q = list(Question.objects.all())
    questions = random.sample(all_q, min(len(all_q), 15))
    return render(request, 'quiz.html', {'questions': questions})