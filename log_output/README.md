# Exercice 1.1

PS C:\uh-cs-devops-with-kubernetes-2026> k3d image import log_output:1.1
INFO[0000] Importing image(s) into cluster 'k3s-default' 
INFO[0000] Saving 1 image(s) from runtime...            
INFO[0001] Importing images into nodes...               
INFO[0001] Importing images from tarball '/k3d/images/k3d-k3s-default-images-20261031031818.tar' into node 'k3d-k3s-default-server-0'... 
INFO[0001] Importing images from tarball '/k3d/images/k3d-k3s-default-images-20261031031818.tar' into node 'k3d-k3s-default-agent-0'... 
INFO[0001] Importing images from tarball '/k3d/images/k3d-k3s-default-images-20261031031818.tar' into node 'k3d-k3s-default-agent-1'... 
INFO[0004] Removing the tarball(s) from image volume... 
                                                        INFO[0005] Removing k3d-tools node...                   
                                                                                                                INFO[0006]Successfully imported image(s)               
                                             INFO[0006] Successfully imported 1 image(s) into 1 cluster(s) 

PS C:\uh-cs-devops-with-kubernetes-2026> kubectl run log-output --image=log_output:1.1
pod/log-output created

PS C:\uh-cs-devops-with-kubernetes-2026> kubectl get pods                             
NAME                                 READY   STATUS    RESTARTS   AGE
hashgenerator-dep-54ddc5f49c-8x4l5   1/1     Running   0          18m
log-output                           1/1     Running   0          3s

PS C:\uh-cs-devops-with-kubernetes-2026> kubectl logs log-output                        
2026-10-31T02:22:19.880013+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:24.880181+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:29.880351+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:34.880527+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:39.879187+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:44.879391+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:49.879588+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:54.879780+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:22:59.879958+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:04.880149+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:09.878993+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:14.879179+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:19.879387+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:24.879616+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:29.879821+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:34.880001+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:39.878806+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:44.879010+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:49.879183+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:54.879362+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:23:59.879537+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:24:04.879716+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:24:09.878228+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:24:14.878409+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54
2026-10-31T02:24:19.878593+00:00: da01e445-a9a2-40a1-84e3-ca5df7cc7c54