using UnityEngine;

public class PlayerControl : MonoBehaviour
{
    void Start()
    {
        
    }

    void Update()
    {
     transform.Translate(Vector3.forward*Time.deltaTime*50);   
    }
}
