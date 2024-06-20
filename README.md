# envoy-cache

### _Caching in Istio using Envoy proxy_

> Easy way to implement Caching in istio using Envoy filter. This working code can cache responses irrespective of the cache control the upstream server sends. 
> The code modifies the cache-control header of the request call and of the upstream response.

## Modifications to be made before using the filter:

1. **Restricting the domain/host over which to apply caching:** Change the domain name (line 29) as per your need. You can also restrict the route/uri over which caching can be applied.
2. **Control the caching time:** Modify the max age of caching by changing the max-age=600 value (line 36 & 89).
3. **The app deployment/pods needs to be enabled in filter for caching:** Change the labels in workload selector to those of the application pods ehich are to be cached (line 71). Also chnge the namespace to where the app pod is deployed (line 67)   
4. There are 2 types of caching in envoy
    * SimpleHTTPCache (line 56)
    * FileSystemHttpCache (line 57-61)
    You can use either of them but not both.

## Demo:

A demo directory is available containing a python app, Dockerfile, K8s & Istio manifest file to test the envoy caching.