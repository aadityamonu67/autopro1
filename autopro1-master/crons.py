#header files

from crontab import CronTab



#cronjobs crud operation
#insert cron
def save_rec_cron(user,command,name,minutes,hours,dom,month,dow):
  my_cron = CronTab(user=user)
  job = my_cron.new(command=command,comment=name)
  job.minute.on(minutes)
  job.hour.on(hours)
  job.day.on(dom)
  job.month.on(month)
  job.dow.on(dow) 
  my_cron.write()


#delete cron
def del_rec_cron(user,name,minutes,hours,dom,month,dow):
	my_cron = CronTab(user=user)
        for job in my_cron:
          if job.comment == str(name):
	     my_cron.remove(job)
             my_cron.write()

#update cron
def upd_rec_cron(user,name,minutes,hours,dom,month,dow):
   my_cron = CronTab(user=user)
   for job in my_cron:
    if job.comment == str(name):
	 job.minute.on(minutes)
         job.hour.on(hours)
         job.day.on(dom)
         job.month.on(month)
         job.dow.on(dow) 
         my_cron.write()
	

#find cron
def find_rec_cron():
	#dont need at this time


#display cron
def disp_rec_cron():
	#dont need at this time

