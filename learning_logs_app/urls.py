''' Defines URL patterns for learning_logs_app'''

from django.urls import path
from learning_logs_app import views


app_name='learning_logs_app'
urlpatterns=[

    path('', views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    
    #page for adding a new topic
    path('new_topic/',views.new_topic,name='new_topic'),

    #page for adding a new entry
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),

    #page for editing an existing entry
    path('edit_entry/<int:entry_id>',views.edit_entry,name='edit_entry'),
]