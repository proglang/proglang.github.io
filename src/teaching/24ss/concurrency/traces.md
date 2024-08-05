Some traces to practice on:

~~~
     T0            T1            
              
e1.   fork(T1)                    
e2.   acq(l1)                      
e3.   wr(x)                       
e4.   rel(l1)                      
e5.   wr(x)                       
e6.                 acq(l1)        
e7.                 wr(x)         
e8.                 rel(l1)        
e9.                 wr(x)
~~~

~~~
     T0            T1            T2            
              
e1.   wr(x)                                     
e2.                 acq(l1)                      
e3.                 rd(x)                       
e4.                 wr(z)                       
e5.                 rel(l1)                      
e6.                               acq(l1)        
e7.                               rel(l1)        
e8.                               wr(x)         
e9.                               wr(y)
~~~

~~~
     T0            T1            
              
e1.                 acq(l1)        
e2.                 rel(l1)        
e3.   acq(l1)                      
e4.   wr(x)                       
e5.   rel(l1)                      
e6.                 rd(x)
~~~

~~~
     T0            T1            
              
e1.   acq(l1)                      
e2.   wr(x)                       
e3.   rel(l1)                      
e4.                 acq(l1)        
e5.                 wr(y)         
e6.                 rel(l1)
~~~

~~~
     T0            T1            
              
e1.   wr(x)                       
e2.   fork(T1)                    
e3.   acq(l1)                      
e4.   rel(l1)                      
e5.                 rd(x)         
e6.                 acq(l1)        
e7.                 rel(l1)
~~~

~~~
     T0            T1            
              
e1.   fork(T1)                    
e2.   acq(l1)                     
e3.   acq(l2)                     
e4.   rel(l2)                     
e5.   rel(l1)                     
e6.                 acq(l2)       
e7.                 acq(l1)       
e8.                 rel(l1)       
e9.                 acq(l1)       
e10.                rel(l1)       
e11.                rel(l2)
~~~

~~~
     T0            T1            T2            T3            
              
e1.   fork(T1)                                                
e2.   fork(T2)                                                
e3.   fork(T3)                                                
e4.                                             acq(l1)       
e5.                                             rel(l1)       
e6.                               acq(l2)                     
e7.                               acq(l3)                     
e8.                               rel(l3)                     
e9.                               rel(l2)                     
e10.                              wr(y)                       
e11.  acq(l1)                                                 
e12.  wr(x)                                                   
e13.  rd(y)                                                   
e14.  rel(l1)                                                 
e15.                acq(l3)                                   
e16.                rd(x)                                     
e17.                acq(l2)                                   
e18.                rel(l2)                                   
e19.                rel(l3) 
~~~