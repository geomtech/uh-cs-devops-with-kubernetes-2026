# Exercice 1.2

```
PS C:\uh-cs-devops-with-kubernetes-2026> kubectl apply -f .\the_course_project\deployment.yaml
deployment.apps/the-course-project created
```

```
PS C:\uh-cs-devops-with-kubernetes-2026> kubectl get pods                                     
NAME                                  READY   STATUS    RESTARTS   AGE
hashgenerator-dep-54ddc5f49c-8x4l5    1/1     Running   0          38m
log-output                            1/1     Running   0          20m
the-course-project-5d898cd9cb-whzww   1/1     Running   0          4s
```

```
PS C:\uh-cs-devops-with-kubernetes-2026> kubectl logs the-course-project-5d898cd9cb-whzww
Server started in port 3000
```