package com.example.cruz.microbuzzapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

/**
 * Created by Cruz on 06/03/2016.
 */
public class LogInActivity extends AppCompatActivity {
    private Button loginUsuario, loginConductor;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        loginConductor =(Button) findViewById(R.id.btn_login_conductor);
        loginUsuario = (Button) findViewById(R.id.btn_login_peaton);

        loginUsuario.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Va a actividad de Usuario
                Intent intentLogged = new Intent(getApplicationContext(),MainActivity.class);
                intentLogged.putExtra("logged","usuario");
                startActivity(intentLogged);
            }
        });
        loginConductor.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intentLogged = new Intent(getApplicationContext(),MainActivity.class);
                intentLogged.putExtra("logged","conductor");
                startActivity(intentLogged);
            }
        });
    }
}
