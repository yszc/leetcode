<?php
class LRUCache {
    private $version;
    private $capacity;
    private $mem;
    private $puts; //0最近的put版本,1最近c个操作几个put
    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->version = 1;
        $this->capacity = $capacity;
    }
  
    /**
     * @param Integer $key
     * @return Integer
     */
    function get($key) {
        echo "get($key)\n";
        var_dump($this->version);
        var_export($this->mem);
        if(isset($this->mem[$key]) && $this->mem[$key][1] > $this->version - $this->capacity - $this->puts ){
            if($this->mem[$key][1] != $this->version){
                $this->version++;
            }
            $this->mem[$key][1] = $this->version;
            return $this->mem[$key][0];
        }else{
            return -1;
        }
        
    }
  
    /**
     * @param Integer $key
     * @param Integer $value
     * @return NULL
     */
    function put($key, $value) {
        if(isset($this->mem[$key]) && $this->mem[$key][1] == $this->version ){
            $this->mem[$key][0] = $value;
        }else{
            $this->mem[$key] = [$value, ++$this->version];
        }
        // return 'n';
    }
}

$client = new LRUCache(3);
echo $client->put (1,1)."\n";  //1
echo $client->put (2,2)."\n";  //21
echo $client->put (3,3)."\n";  //321
echo $client->put (4,4)."\n";  //432 1
echo $client->get (4)."\n";    //432
echo $client->get (3)."\n";    //342
echo $client->get (2)."\n";    //234
echo $client->get (1)."\n";
echo $client->put (5,5)."\n";
echo $client->get (1)."\n";
echo $client->get (2)."\n";
echo $client->get (3)."\n";
echo $client->get (4)."\n";
echo $client->get (5)."\n";
 

// $client = new LRUCache(2);
// echo $client->get (2)."\n";
// echo $client->put (2,6)."\n";
// echo $client->get (1)."\n";
// echo $client->get (1)."\n";
// echo $client->get (1)."\n";
// echo $client->get (1)."\n";
// echo $client->put (1,5)."\n";
// echo $client->put (1,2)."\n";
// echo $client->get (1)."\n";
// echo $client->get (2)."\n";


// $client = new LRUCache(2);
// echo $client->put (1,1)."\n";  //1-1
// echo $client->put (2,2)."\n";  //2-21
// echo $client->get (1)."\n";    //3-12
// echo $client->put (3,3)."\n";  //4-31 2
// echo $client->get (2)."\n";    //
// echo $client->put (4,4)."\n";
// echo $client->get (1)."\n";
// echo $client->get (3)."\n";
// echo $client->get (4)."\n";