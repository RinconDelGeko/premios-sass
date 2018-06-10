<form class="needs-validation" novalidate>
  <h2>Editar Perfil</h2>
  <div class="row">
    <div class="col-md-4">
      <img src="/static/img/chompy.jpg" alt="UserIMG" class="img-fluid img-thumbnail">
    </div>
    <div class="col-md-8">
      <div class="form-row">
        <div class="col-md-8 mb-3">
          <label for="fullName">Nombre</label>
          <input type="text" class="form-control" id="fullName" required>
          <div class="invalid-feedback">
            El nombre no es válido 
          </div>
        </div>
      </div>
      <div class="form-row">
        <div class="col-md-8 mb-3">
          <label for="userName">Usuario</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <div class="input-group-text">@</div>
            </div>
            <input type="text" class="form-control" id="userName" required>
          </div>
          <div class="invalid-feedback">
            Usuario no valido
          </div>
        </div>
      </div>
      <div class="form-row">
        <div class="col-md-8 mb-3">
          <label for="userEmail">Correo</label>
          <input type="text" class="form-control" id="userEmail" required>
          <div class="invalid-feedback">
            Email no válido
          </div>
        </div>
      </div>
    </div>
  </div>
  <br>
  <hr>
  <h4>Modificar Contraseña</h4>
  <div class="row">
    <div class="col-4">
      <label for="userPassword1">Nueva Contraseña</label>
      <input type="password" id="userPassword1" class="form-control">
    </div>
  </div>
  <div class="row">
    <div class="col-4">
      <label for="userPassword2">Repetir Contraseña</label>
      <input type="password" id="userPassword2" class="form-control">
    </div>
  </div>
  <br>
  <hr>
  <button class="btn btn-primary" type="submit">Guardar</button>
  <button class="btn btn-danger" type="submit">Cancelar</button>
</form>

<script>
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
</script>