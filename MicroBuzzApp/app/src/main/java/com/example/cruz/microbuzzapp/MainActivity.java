package com.example.cruz.microbuzzapp;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.view.Menu;
import android.view.MenuItem;

import com.example.cruz.microbuzzapp.uifragments.PantallaConductorFragment;
import com.example.cruz.microbuzzapp.uifragments.PantallaPeatonFragment;

public class MainActivity extends AppCompatActivity {
    private String userLogged;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Dependiendo de la seleccion de usuario Conductor
        // o usuario peaton reemplazamos el fragment.
        userLogged = getIntent().getStringExtra("logged");
        eligePantallaUsuario(userLogged);
    }
    // Cambia entre fragmentos.
    public void eligePantallaUsuario(String userLogged){
        if(TextUtils.equals(userLogged,"conductor")){
            replaceFragment( new PantallaConductorFragment());
        }else{
            replaceFragment( new PantallaPeatonFragment() );
        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }
        if (id == R.id.action_log_out) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
    public void replaceFragment(Fragment fragment){
        FragmentManager fragmentManager = getSupportFragmentManager();
        FragmentTransaction transaction = fragmentManager.beginTransaction();
        transaction.replace(R.id.container,fragment);
        transaction.commit();
    }
}
